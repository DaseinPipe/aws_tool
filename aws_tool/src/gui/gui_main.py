import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem, QMessageBox
import time
from PySide2.QtCore import Qt
from contextlib import contextmanager
from aws_tool.src.resource import resource_main, message_box
from aws_tool.src.config.config_main import *
import boto3


def cell_editable(item, status=False):
    flags = item.flags()
    if status:
        flags |= Qt.ItemIsEditable
    else:
        flags &= ~Qt.ItemIsEditable
    item.setFlags(flags)


@contextmanager
def wait_cursor():
    try:
        QApplication.setOverrideCursor(Qt.WaitCursor)
        yield
    finally:
        QApplication.restoreOverrideCursor()


class AwsMain(resource_main.Ui_MainWindow, QMainWindow):

    def __init__(self, ):
        super(AwsMain, self).__init__()
        self.setupUi(self)
        self.main_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.main_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.instance_column_name = 'Instance'
        self.ec2_client = boto3.client('ec2', region_name='ap-south-1')
        self.instance_response = self.ec2_client.describe_instances()
        self._instance_status = UNKNOWN
        self.populate()
        self.connection()

    def populate(self):
        self.main_tableWidget.setRowCount(0)
        for instance_data in self.aws_instances_list:
            instance = instance_data.get(self.instance_column_name)
            self.instance_status = instance
            instance_data['InstanceState'] = self.instance_status
            self.add_row(row_data=instance_data.copy())

    def connection(self):
        self.refresh_pushButton.clicked.connect(self.refresh)
        self.start_pushButton.clicked.connect(self.start_instance)
        self.stop_pushButton.clicked.connect(self.stop_instance)

    def refresh(self):
        self.populate()

    def get_instance(self):
        main_tableWidget = self.main_tableWidget
        for item in self.main_tableWidget.selectedItems():
            horizontal_header_item = main_tableWidget.horizontalHeaderItem(item.column())
            column_name = horizontal_header_item.text()
            if column_name == self.instance_column_name:
                return item.text()
        message_box.pop_up(
            messType='info',
            messTitle='Instance Not Found.',
            messText='Please select row and retry',
            buttons=QMessageBox.Cancel,
            defaultButton=QMessageBox.Cancel
        )
        return

    def start_instance(self):
        instance = self.get_instance()
        if not instance:
            return
        self.ec2_client.start_instances(InstanceIds=[instance])
        with wait_cursor():
            time.sleep(30)
            self.refresh()
        message_box.pop_up(
            messType='info',
            messTitle='Instance Started.',
            messText=f"Successfully started instances: {instance} ",
            buttons=QMessageBox.Cancel,
            defaultButton=QMessageBox.Cancel
        )

    def stop_instance(self):
        instance = self.get_instance()
        if not instance:
            return
        self.ec2_client.stop_instances(InstanceIds=[instance])
        with wait_cursor():
            time.sleep(20)
            self.refresh()
        message_box.pop_up(
            messType='info',
            messTitle='Instance Stopped.',
            messText=f"Successfully stopped instances: {instance} ",
            buttons=QMessageBox.Cancel,
            defaultButton=QMessageBox.Cancel
        )

    def insert_row(self, current_row, current_column, value):
        source_item = QTableWidgetItem(value)
        cell_editable(source_item, False)
        self.main_tableWidget.setItem(current_row, current_column, source_item)

    def get_column_no(self, column_name):
        main_tableWidget = self.main_tableWidget
        for column in range(0, main_tableWidget.columnCount()):
            if not main_tableWidget.horizontalHeaderItem(column):
                return 1
            if column_name == main_tableWidget.horizontalHeaderItem(column).text():
                return column

    def add_row(self, row_data):
        current_row = self.main_tableWidget.rowCount()
        self.main_tableWidget.insertRow(current_row)
        for column_name, value in row_data.items():
            current_column = self.get_column_no(column_name)
            self.insert_row(current_row, current_column, value)

    @property
    def instance_status(self):
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance):
        status_response = self.ec2_client.describe_instance_status(InstanceIds=[instance])
        if not status_response.get('InstanceStatuses'):
            self._instance_status = 'stopped'
        else:
            status = status_response['InstanceStatuses'][0]['InstanceState']['Name']
            self._instance_status = status

    @property
    def aws_instances_list(self):
        instance_list = []
        for r in self.instance_response['Reservations']:
            for instance in r['Instances']:
                instance_list.append(
                    {
                        'Name': instance['Tags'][0]['Value'],
                        'PublicIpAddress': instance.get('PublicIpAddress', ''),
                        'Instance': instance['InstanceId'],
                    }
                )
        return instance_list


def run():
    app = QApplication(sys.argv)
    with open(stylesheet_path, 'r') as FID:
        qss = FID.read()
        app.setStyleSheet(qss)
    w = AwsMain()
    w.show()
    app.exec_()


if __name__ == '__main__':
    run()
