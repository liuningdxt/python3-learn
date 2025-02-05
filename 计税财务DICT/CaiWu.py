import datetime
import math
import sys
from builtins import print

import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QFont, QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QFileDialog, QMessageBox, QLabel, QHBoxLayout

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# PyQt5 主窗口
class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("效益分析表财务金额核对")
        self.setGeometry(100, 100, 2000, 1200)

        # 创建一个 QTableWidget 控件，填充效益表计算数据
        self.table = QTableWidget(self)
        self.fill_table(self.table)

        # 创建第一个表格
        self.table1 = QTableWidget(self)
        self.table1.setRowCount(3)
        self.table1.setColumnCount(8)
        # self.table1.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3', 'Column 4'])
        self.table1.setFixedSize(1800, 200)  # 固定大小
        self.fill_table(self.table1)
        self.merge_cells(self.table1)
        # 设置列自适应宽度
        self.table1.resizeColumnsToContents()
        # 加粗表格线条和字体
        self.apply_bold_styles(self.table1)

        # 创建按钮，点击按钮加载 Excel 文件
        self.button = QPushButton('导入效益表', self)
        self.button.clicked.connect(self.load_excel)
        self.button.setFixedSize(200, 50)

        # 创建 QLabel 控件显示文件名称
        self.file_label = QLabel('未选中文件', self)
        self.file_label.setAlignment(Qt.AlignCenter)
        # 设置标签的固定大小（宽度：300，高度：50）
        self.file_label.setFixedSize(600, 50)

        # 标签用于显示拖放提示
        self.label = QLabel("方法1：拖动效益表Excel文件到此窗口" + "\n"
                                                                  "方法2：点击导入------>效益表按钮，选择文件导入", self)
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.label.setFont(font)

        # 创建水平布局，将按钮和标签并排显示
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.label)  # 添加拖放提示标签
        h_layout.addStretch(1)
        h_layout.addWidget(self.button)  # 添加按钮
        h_layout.addWidget(self.file_label)  # 添加标签

        # 创建一个垂直布局（以便进一步添加其他控件）
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)  # 添加水平布局（包含按钮和标签）
        v_layout.addWidget(self.table1)  # 添加表格到布局
        v_layout.addWidget(self.table)  # 添加表格到布局

        # 创建一个QWidget容器，并设置为主窗口的中央部件
        container = QWidget()
        container.setLayout(v_layout)
        self.setCentralWidget(container)

        # 禁用所有单元格的编辑功能
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table1.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table1.setFocusPolicy(Qt.NoFocus)

        # 启用拖放功能
        self.setAcceptDrops(True)

    # 事件：拖动进入窗口时
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    # 事件：文件被放下时
    def dropEvent(self, event: QDropEvent):
        file_url = event.mimeData().urls()[0].toLocalFile()
        if file_url.endswith(".xlsx") | file_url.endswith(".xls"):
            self.parse_excel(file_url)
        else:
            self.label.setText("只支持 excel 文件格式")

    # 解析 CSV 文件并显示在表格中
    def parse_excel(self, file_path):
        try:
            if file_path:
                # 使用 pandas 读取 Excel 文件并加载为 DataFrame
                # 显示 DataFrame 的内容在 QTableWidget 中
                self.display_df_in_table(file_path)

            self.label.setText(f"成功加载文件: {file_path}")
        except Exception as e:
            self.label.setText(f"文件加载失败: {str(e)}")

    def fill_table(self, table_widget):
        for row in range(table_widget.rowCount()):
            for col in range(table_widget.columnCount()):
                item = QTableWidgetItem('')
                table_widget.setItem(row, col, item)

    def apply_bold_styles(self, table_widget):
        # 加粗表格线条
        table_widget.setStyleSheet("""
            QTableWidget {
                border: 2px solid black;  /* 设置表格边框的粗细 */
            }
            QTableWidget::item {
                border: 1px solid black;  /* 设置单元格边框的粗细 */
            }
            QHeaderView::section {
                background-color: lightgray;  /* 设置表头背景颜色 */
                font-weight: bold;  /* 设置表头字体加粗 */
                border: 1px solid black;  /* 设置表头边框 */
            }
        """)

    def merge_cells(self, table_widget):
        """合并单元格并填充数据"""
        # 合并第一行的第 1 到第 3 列
        font = QFont()
        font.setBold(True)
        table_widget.setItem(0, 0, QTableWidgetItem("项目名称"))
        table_widget.item(0, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(0, 0).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(0, 0).setFont(font)

        table_widget.setItem(1, 0, QTableWidgetItem("项目客户单位"))
        table_widget.item(1, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(1, 0).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(1, 0).setFont(font)

        table_widget.setItem(2, 0, QTableWidgetItem("项目合作单位"))
        table_widget.item(2, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(2, 0).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(2, 0).setFont(font)

        table_widget.setItem(0, 2, QTableWidgetItem("净现值率（%）—决策指标"))
        table_widget.item(0, 2).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(0, 2).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(0, 2).setFont(font)

        table_widget.item(0, 3).setForeground(QBrush(QColor(0, 0, 0)))  # 设置文本黑色
        table_widget.item(0, 3).setFont(font)

        table_widget.setItem(1, 2, QTableWidgetItem("项目经理"))
        table_widget.item(1, 2).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(1, 2).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(1, 2).setFont(font)

        table_widget.setItem(2, 2, QTableWidgetItem("联系电话"))
        table_widget.item(2, 2).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(2, 2).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(2, 2).setFont(font)

        table_widget.setItem(0, 4, QTableWidgetItem("建设周期（月）"))
        table_widget.item(0, 4).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(0, 4).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(0, 4).setFont(font)

        table_widget.setItem(1, 4, QTableWidgetItem("合作/维护周期（月）"))
        table_widget.item(1, 4).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(1, 4).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(1, 4).setFont(font)

        table_widget.setItem(2, 4, QTableWidgetItem("IT资产权属"))
        table_widget.item(2, 4).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(2, 4).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(2, 4).setFont(font)

        table_widget.setItem(0, 6, QTableWidgetItem("建设期间"))
        table_widget.item(0, 6).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(0, 6).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(0, 6).setFont(font)

        table_widget.setItem(1, 6, QTableWidgetItem("合作/维护期间"))
        table_widget.item(1, 6).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(1, 6).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(1, 6).setFont(font)

        table_widget.setItem(2, 6, QTableWidgetItem("合作模式"))
        table_widget.item(2, 6).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        table_widget.item(2, 6).setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
        table_widget.item(2, 6).setFont(font)

    def load_excel(self):
        # 打开文件选择对话框，选择 Excel 文件
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "",
                                                   "Excel Files (*.xls *.xlsx);;All Files (*)", options=options)

        if file_path:
            try:
                # 更新 QLabel 显示文件名称
                self.file_label.setText(f"效益表文件名: {file_path.split('/')[-1]}")

                # 使用 pandas 读取 Excel 文件并加载为 DataFrame
                # 显示 DataFrame 的内容在 QTableWidget 中
                self.display_df_in_table(file_path)
            except Exception as e:
                # 如果读取文件出错，弹出错误提示框
                QMessageBox.critical(self, "Error", f"Failed to load Excel file: {str(e)}")

    def display_df_in_table(self, filePath):
        df = pd.read_excel(filePath, sheet_name='现金流明细表（集客填报）', usecols='E:G', header=7)
        df.loc[df['Unnamed: 4'] == '9、招投标服务费、标书制作费等', 'Unnamed: 5'] = 0
        df.dropna(inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.rename(columns={'Unnamed: 4': '类别', 'Unnamed: 5': '税率_集客', 'Unnamed: 6': '含税金额'}, inplace=True)
        df_count = pd.read_excel(filePath, sheet_name='现金流明细表（集客填报）', usecols='E:DO', header=7)
        df_count.dropna(how='all', inplace=True)
        # 删除科目，税率是空的数据。剔除税率，汇总金额列
        df_count.loc[df_count['Unnamed: 4'] == '9、招投标服务费、标书制作费等', 'Unnamed: 5'] = 0
        df_count.dropna(subset=['Unnamed: 5'], inplace=True)
        df_count.drop(columns=['Unnamed: 5', 'Unnamed: 6'], inplace=True)
        df_count.dropna(subset=['Unnamed: 4'], inplace=True)
        df_count.rename(columns={'Unnamed: 4': '类别'}, inplace=True)
        # 设置为索引
        df_count.set_index('类别', inplace=True)
        df_count.fillna(0, inplace=True)
        # 统计每个科目在每个月金额大于0的次数
        df_count_cal = (df_count > 0).sum(axis=1)
        # 输出金额大于0的次数
        df_count_cal = df_count_cal.reset_index()
        df_count_cal.columns = ['类别', '集客-月份数']
        index_to_drop = df_count_cal[df_count_cal['类别'] == '1、 集成-信息服务'].index
        df_count_cal.drop(index_to_drop, inplace=True)
        df_count_cal = df_count_cal.reset_index(drop=True)
        df_count_cal['索引'] = df_count_cal.index

        # 删除无效行
        index_to_drop = df[df['类别'] == '1、 集成-信息服务'].index
        df.drop(index_to_drop, inplace=True)
        df.reset_index(drop=True, inplace=True)
        print("1-开始读取文件-集客")
        print("1-1开始读取文件-集客-计算不含税金额")
        df['不含税金额-正确计算'] = (df['含税金额'] / (1 + df['税率_集客']))
        df['不含税金额-正确计算'] = df['不含税金额-正确计算'].astype(float)
        df['不含税金额-正确计算'] = df['不含税金额-正确计算'].round(2)
        print("1-1结束读取文件-集客-计算不含税金额")
        print("1-结束读取文件-集客")

        print("2-开始读取文件-财务")
        df_cw = pd.read_excel(filePath, sheet_name='财务列账明细表（财务填报）', usecols='E:G', header=7)
        df_cw.loc[df_cw['Unnamed: 4'] == '9、招投标服务费、标书制作费等', 'Unnamed: 5'] = 0
        df_cw.rename(columns={'Unnamed: 4': '类别_财务', 'Unnamed: 5': '税率_财务', 'Unnamed: 6': '不含税金额_财务表'},
                     inplace=True)
        df_cw.dropna(inplace=True)
        df_cw.reset_index(drop=True, inplace=True)

        df_cw_count = pd.read_excel(filePath, sheet_name='财务列账明细表（财务填报）', usecols='E:DO', header=7)
        df_cw_count.dropna(how='all', inplace=True)
        df_cw_count.loc[df_cw_count['Unnamed: 4'] == '9、招投标服务费、标书制作费等', 'Unnamed: 5'] = 0
        # 删除科目，税率是空的数据。剔除税率，汇总金额列
        df_cw_count.dropna(subset=['Unnamed: 5'], inplace=True)
        df_cw_count.drop(columns=['Unnamed: 5', 'Unnamed: 6'], inplace=True)
        df_cw_count.dropna(subset=['Unnamed: 4'], inplace=True)
        df_cw_count.rename(columns={'Unnamed: 4': '类别'}, inplace=True)
        # 设置为索引
        df_cw_count.set_index('类别', inplace=True)
        df_cw_count.fillna(0, inplace=True)
        df_cw_count['Unnamed: 7'] = df_cw_count['Unnamed: 7'].astype(float)
        # 统计每个科目在每个月金额大于0的次数
        df_cw_count_cal = (df_cw_count > 0).sum(axis=1)
        # 输出金额大于0的次数
        df_cw_count_cal = df_cw_count_cal.reset_index()
        df_cw_count_cal.columns = ['类别', '财务-月份数']
        index_to_drop = df_cw_count_cal[
            ((df_cw_count_cal['类别'] == '1、 集成收入-信息服务') | (df_cw_count_cal['类别'] == '10、垫资成本') | (
                    df_cw_count_cal[
                        '类别'] == '10-1 垫资金额'))].index
        df_cw_count_cal.drop(index_to_drop, inplace=True)
        df_cw_count_cal = df_cw_count_cal.reset_index(drop=True)
        df_cw_count_cal['索引'] = df_cw_count_cal.index

        # 删除无效行
        index_to_drop = df_cw[
            ((df_cw['类别_财务'] == '1、 集成收入-信息服务') | (df_cw['类别_财务'] == '10、垫资成本') | (df_cw[
                                                                                                           '类别_财务'] == '10-1 垫资金额'))].index
        df_cw.drop(index_to_drop, inplace=True)
        df_cw.reset_index(drop=True, inplace=True)
        print("2-结束读取文件-财务")
        df['索引'] = df.index
        df_cw['索引'] = df_cw.index
        df_a = pd.merge(df, df_count_cal, on='索引', how='left', suffixes=('_集客', '_集客1'))
        df_a = df_a[['类别_集客', '集客-月份数', '税率_集客', '含税金额', '不含税金额-正确计算', '索引']]

        df_b = pd.merge(df_cw, df_cw_count_cal, on='索引', how='left', suffixes=('_财务', '_财务1'))
        df_b = df_b[['类别_财务', '财务-月份数', '税率_财务', '不含税金额_财务表', '索引']]

        merged_df = pd.merge(df_a, df_b, on='索引', how='inner')
        # 比较两个列是否相同
        columns_are_equal = df['不含税金额-正确计算'].equals(df_cw['不含税金额_财务表'])

        # 清空现有的表格内容
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

        # 设置表格行列数
        self.table.setRowCount(len(merged_df))
        self.table.setColumnCount(len(merged_df.columns))

        # 设置表头
        self.table.setHorizontalHeaderLabels(merged_df.columns)
        font = QFont()
        font.setBold(True)
        self.table.horizontalHeaderItem(4).setFont(font)
        self.table.horizontalHeaderItem(4).setForeground(QBrush(QColor(255, 0, 0)))
        self.table.horizontalHeaderItem(9).setFont(font)
        self.table.horizontalHeaderItem(9).setForeground(QBrush(QColor(255, 0, 0)))

        # 填充表格数据
        for row_idx, row in merged_df.iterrows():
            for col_idx, value in enumerate(row):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        # 设置列自适应宽度
        self.table.resizeColumnsToContents()

        # 比较 金额 列，并根据比较结果改变颜色
        self.compare_and_mark_colors()

        self.add_column()

        # 设置表格样式
        self.table.setStyleSheet("""
                                    QTableWidget {
                                        border: 1px solid black;  /* 设置表格外边框 */
                                    }
                                    QHeaderView::section {
                                        border: 1px solid black;  /* 设置表头边框 */
                                    }
                                    QTableWidget::item:selected {
                                        background-color: #87CEFA;  /* 设置选中项的背景色为浅蓝色 */
                                    }
                                    """
                                 )

        # 自动调整行高
        self.table.resizeRowsToContents()

        table_widget = self.table1
        df_project = pd.read_excel(filePath, sheet_name='综合评估表', usecols='B:J', header=3)
        value = df_project.iloc[0, 1]
        if value is None:
            value = '空'
        table_widget.setItem(0, 1, QTableWidgetItem(value))
        table_widget.item(0, 1).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = df_project.iloc[1, 1]
        table_widget.setItem(1, 1, QTableWidgetItem(value))
        table_widget.item(1, 1).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = df_project.iloc[2, 1]
        if type(value) == float and math.isnan(value):
            value = '空'
        table_widget.setItem(2, 1, QTableWidgetItem(value))
        table_widget.item(2, 1).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = str(round(float(df_project.iloc[6, 1]) * 100, 4)) + '%'
        table_widget.setItem(0, 3, QTableWidgetItem(value))
        table_widget.item(0, 3).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = df_project.iloc[1, 3]
        table_widget.setItem(1, 3, QTableWidgetItem(value))
        table_widget.item(1, 3).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = str(df_project.iloc[2, 3])
        table_widget.setItem(2, 3, QTableWidgetItem(value))
        table_widget.item(2, 3).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = str(df_project.iloc[0, 6])
        table_widget.setItem(0, 5, QTableWidgetItem(value))
        table_widget.item(0, 5).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = str(df_project.iloc[1, 6])
        table_widget.setItem(1, 5, QTableWidgetItem(value))
        table_widget.item(1, 5).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = df_project.iloc[2, 6]
        table_widget.setItem(2, 5, QTableWidgetItem(value))
        table_widget.item(2, 5).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = df_project.iloc[0, 8]
        if type(value) is datetime.datetime:
            value = value.strftime("%Y年%m月")
        elif type(value) is str:
            value = value
        table_widget.setItem(0, 7, QTableWidgetItem(value))
        table_widget.item(0, 7).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = df_project.iloc[1, 8]
        table_widget.setItem(1, 7, QTableWidgetItem(value))
        table_widget.item(1, 7).setTextAlignment(Qt.AlignCenter)  # 设置文本居中

        value = df_project.iloc[2, 8]
        table_widget.setItem(2, 7, QTableWidgetItem(value))
        table_widget.item(2, 7).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table1.resizeColumnsToContents()

    def compare_and_mark_colors(self):
        # 获取数据表格的行数
        row_count = self.table.rowCount()

        font = QFont()
        font.setBold(True)

        # 遍历所有行并进行比较
        for row_idx in range(row_count):
            type_item = self.table.item(row_idx, 0)
            amount_item = self.table.item(row_idx, 4)
            compare_item = self.table.item(row_idx, 9)
            # 确保项不为空
            if amount_item and compare_item:
                amount = float(amount_item.text())
                compare_amount = float(compare_item.text())

                # 比较并标记颜色
            if amount == compare_amount:
                None
                # 如果相同，设置绿色背景
                # amount_item.setBackground(QBrush(QColor(144, 238, 144)))  # Green
                # amount_item.setForeground(QBrush(QColor(0, 0, 255)))  # 设置文本红色
                # compare_item.setBackground(QBrush(QColor(144, 238, 144)))  # Green
                # compare_item.setForeground(QBrush(QColor(0, 0, 255)))  # 设置文本红色
            else:
                # 如果不同，设置红色背景
                amount_item.setBackground(QBrush(QColor(255, 182, 193)))  # Red
                amount_item.setForeground(QBrush(QColor(255, 0, 0)))  # 设置文本红色
                # amount_item.setBackground(QColor(255, 0, 0))
                # compare_item.setBackground(QColor(0, 0, 255))
                compare_item.setBackground(QBrush(QColor(255, 182, 193)))  # Red
                compare_item.setForeground(QBrush(QColor(255, 0, 0)))  # Red
                type_item.setForeground(QBrush(QColor(255, 0, 0)))
                type_item.setBackground(QBrush(QColor(255, 182, 193)))  # Red
                amount_item.setFont(font)
                compare_item.setFont(font)
                type_item.setFont(font)

    def add_column(self):
        # 增加一列到最前面
        self.table.insertColumn(0)  # 将新列插入到索引0（最前面）
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("二级分类"))

        # 填充新列的数据
        for row in range(self.table.rowCount()):
            self.table.setItem(row, 0, QTableWidgetItem(f"New{row + 1}"))

        # 合并新列的单元格（假设要将新列的所有单元格合并为一个单元格）
        self.table.setItem(0, 0, QTableWidgetItem("\n".join(f"IT现金流入")))
        self.table.item(0, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(0, 0, 26, 1)  # 合并最前面一列的所有行

        self.table.setItem(26, 0, QTableWidgetItem("\n".join(f"CT现金流入")))
        self.table.item(26, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(26, 0, 13, 1)  # 合并最前面一列的所有行

        self.table.setItem(39, 0, QTableWidgetItem("\n".join(f"往来款现金流入")))
        self.table.item(39, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(39, 0, 8, 1)  # 合并最前面一列的所有行

        self.table.setItem(47, 0, QTableWidgetItem("\n".join(f"平台类流出")))
        self.table.item(47, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(47, 0, 6, 1)  # 合并最前面一列的所有行

        self.table.setItem(53, 0, QTableWidgetItem("\n".join(f"传输网络配套流出")))
        self.table.item(53, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(53, 0, 1, 1)  # 合并最前面一列的所有行

        self.table.setItem(54, 0, QTableWidgetItem("\n".join(f"IT现金流出")))
        self.table.item(54, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(54, 0, 11, 1)  # 合并最前面一列的所有行

        self.table.setItem(65, 0, QTableWidgetItem("\n".join(f"间接现金流出")))
        self.table.item(65, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(65, 0, 4, 1)  # 合并最前面一列的所有行

        self.table.setItem(69, 0, QTableWidgetItem("\n".join(f"往来款现金流出")))
        self.table.item(69, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(69, 0, 9, 1)  # 合并最前面一列的所有行

        self.table.insertColumn(0)  # 将新列插入到索引0（最前面）
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("一级分类"))

        self.table.setItem(0, 0, QTableWidgetItem("\n".join(f"现金流入")))
        self.table.item(0, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(0, 0, 47, 1)  # 合并最前面一列的所有行

        self.table.setItem(47, 0, QTableWidgetItem('投资现金流出' + '\n' + '（Capex）'))
        self.table.item(47, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(47, 0, 7, 1)  # 合并最前面一列的所有行

        self.table.setItem(54, 0, QTableWidgetItem('成本现金流出' + '\n' + '（Opex）'))
        self.table.item(54, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(54, 0, 15, 1)  # 合并最前面一列的所有行

        self.table.setItem(69, 0, QTableWidgetItem("\n".join(f"往来款现金流出")))
        self.table.item(69, 0).setTextAlignment(Qt.AlignCenter)  # 设置文本居中
        self.table.setSpan(69, 0, 9, 1)  # 合并最前面一列的所有行


# 运行应用程序
app = QApplication(sys.argv)
window = TableWindow()
window.show()
sys.exit(app.exec_())
