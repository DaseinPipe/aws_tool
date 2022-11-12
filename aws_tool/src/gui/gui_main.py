import sys
import ast
import subprocess
from PySide2.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem, QMessageBox
from PySide2.QtCore import Qt
from aws_tool.src.resource import resource_main, message_box
from aws_tool.src.config.config_main import *


def cell_editable(item, status=False):
    flags = item.flags()
    if status:
        flags |= Qt.ItemIsEditable
    else:
        flags &= ~Qt.ItemIsEditable
    item.setFlags(flags)


class AwsMain(resource_main.Ui_MainWindow, QMainWindow):

    def __init__(self, ):
        super(AwsMain, self).__init__()
        self.setupUi(self)
        self.main_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.main_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.instance_column_name = 'Instance'
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
        instance_start_cmd = f'''
            aws ec2 start-instances \
            --region ap-south-1 \
            --instance-ids {instance}
        '''
        subprocess.call([instance_start_cmd], shell=True)
        result = subprocess.check_output(
            [instance_start_cmd],
            shell=True
        ).decode('UTF-8').replace('null', 'None')
        self.refresh()
        message_box.pop_up(
            messType='info',
            messTitle='Instance Started.',
            messText=result,
            buttons=QMessageBox.Cancel,
            defaultButton=QMessageBox.Cancel
        )



    def stop_instance(self):
        instance = self.get_instance()
        if not instance:
            return
        instance_stop_cmd = f'''
            aws ec2 stop-instances \
            --region ap-south-1 \
            --instance-ids {instance}
        '''
        result = subprocess.check_output(
            [instance_stop_cmd],
            shell=True
        ).decode('UTF-8').replace('null', 'None')
        result = ast.literal_eval(result)
        self.refresh()
        message_box.pop_up(
            messType='info',
            messTitle='Instance Stopped.',
            messText=str(result),
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
        instance_status_query_cmd = f'''
            aws ec2 describe-instance-status \
            --region ap-south-1 \
            --instance-id {instance}

        '''
        result = subprocess.check_output([instance_status_query_cmd], shell=True).decode('UTF-8').replace('null',
                                                                                                          'None')
        result = ast.literal_eval(result)
        if not result.get('InstanceStatuses'):
            self._instance_status = 'stopped'
        else:
            status = result.get('InstanceStatuses')[0].get('InstanceState', {}).get('Name', UNKNOWN)
            self._instance_status = status

    @property
    def aws_instances_list(self):
        instances_query_cmd = '''
           aws ec2 describe-instances \
           --region ap-south-1 \
           --filters Name=tag-key,Values=Name,ip-address \
           --query 'Reservations[*].Instances[*].{Instance:InstanceId,PublicIpAddress:PublicIpAddress,Name:Tags[?Key==`Name`]|[0].Value}' \
           --output json
        '''
        result = subprocess.check_output([instances_query_cmd], shell=True).decode('UTF-8').replace('null', 'None')
        return [each[0] for each in ast.literal_eval(result)]


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
