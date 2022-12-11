# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'retool-settings.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
from  . import resources_rc

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(601, 360)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMinimumSize(QSize(601, 360))
        Settings.setMaximumSize(QSize(601, 360))
        self.gridLayoutWidget = QWidget(Settings)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, -1, 601, 361))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setContentsMargins(15, 15, 15, 0)
        self.labelCloneListMetadataDownloadURL = QLabel(self.gridLayoutWidget)
        self.labelCloneListMetadataDownloadURL.setObjectName(u"labelCloneListMetadataDownloadURL")
        self.labelCloneListMetadataDownloadURL.setMaximumSize(QSize(16777215, 18))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        self.labelCloneListMetadataDownloadURL.setFont(font)

        self.gridLayout.addWidget(self.labelCloneListMetadataDownloadURL, 8, 0, 1, 1)

        self.frameCloneListsLocation = QFrame(self.gridLayoutWidget)
        self.frameCloneListsLocation.setObjectName(u"frameCloneListsLocation")
        self.frameCloneListsLocation.setMinimumSize(QSize(0, 41))
        self.frameCloneListsLocation.setMaximumSize(QSize(16777215, 41))
        self.frameCloneListsLocation.setFrameShape(QFrame.StyledPanel)
        self.frameCloneListsLocation.setFrameShadow(QFrame.Raised)
        self.buttonChooseCloneListsLocation = QPushButton(self.frameCloneListsLocation)
        self.buttonChooseCloneListsLocation.setObjectName(u"buttonChooseCloneListsLocation")
        self.buttonChooseCloneListsLocation.setGeometry(QRect(0, 0, 41, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.buttonChooseCloneListsLocation.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/retoolFiles/images/icons8-live-folder-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonChooseCloneListsLocation.setIcon(icon)
        self.buttonChooseCloneListsLocation.setIconSize(QSize(32, 32))
        self.buttonChooseCloneListsLocation.setAutoDefault(False)
        self.labelSelectCloneListsLocation = QLabel(self.frameCloneListsLocation)
        self.labelSelectCloneListsLocation.setObjectName(u"labelSelectCloneListsLocation")
        self.labelSelectCloneListsLocation.setGeometry(QRect(50, 0, 531, 16))
        self.labelSelectCloneListsLocation.setFont(font)
        self.labelCloneListsLocation = QLabel(self.frameCloneListsLocation)
        self.labelCloneListsLocation.setObjectName(u"labelCloneListsLocation")
        self.labelCloneListsLocation.setGeometry(QRect(50, 20, 531, 20))
        palette = QPalette()
        brush = QBrush(QColor(119, 119, 119, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.labelCloneListsLocation.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        self.labelCloneListsLocation.setFont(font2)

        self.gridLayout.addWidget(self.frameCloneListsLocation, 3, 0, 1, 1)

        self.labelPaths = QLabel(self.gridLayoutWidget)
        self.labelPaths.setObjectName(u"labelPaths")
        self.labelPaths.setMinimumSize(QSize(0, 18))
        self.labelPaths.setMaximumSize(QSize(16777215, 18))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        self.labelPaths.setFont(font3)
        self.labelPaths.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.labelPaths, 1, 0, 1, 1)

        self.labelDownloadLocations = QLabel(self.gridLayoutWidget)
        self.labelDownloadLocations.setObjectName(u"labelDownloadLocations")
        self.labelDownloadLocations.setMinimumSize(QSize(0, 18))
        self.labelDownloadLocations.setMaximumSize(QSize(16777215, 18))
        self.labelDownloadLocations.setFont(font3)
        self.labelDownloadLocations.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.labelDownloadLocations, 6, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.lineDownloadLocations = QFrame(self.gridLayoutWidget)
        self.lineDownloadLocations.setObjectName(u"lineDownloadLocations")
        palette1 = QPalette()
        brush3 = QBrush(QColor(85, 85, 85, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.lineDownloadLocations.setPalette(palette1)
        self.lineDownloadLocations.setFrameShadow(QFrame.Plain)
        self.lineDownloadLocations.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.lineDownloadLocations, 7, 0, 1, 1)

        self.linePaths = QFrame(self.gridLayoutWidget)
        self.linePaths.setObjectName(u"linePaths")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.linePaths.setPalette(palette2)
        self.linePaths.setFrameShadow(QFrame.Plain)
        self.linePaths.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.linePaths, 2, 0, 1, 1)

        self.frameResetButton = QFrame(self.gridLayoutWidget)
        self.frameResetButton.setObjectName(u"frameResetButton")
        self.frameResetButton.setMinimumSize(QSize(0, 25))
        self.frameResetButton.setMaximumSize(QSize(16777215, 25))
        self.frameResetButton.setFrameShape(QFrame.NoFrame)
        self.frameResetButton.setFrameShadow(QFrame.Plain)
        self.pushButtonReset = QPushButton(self.frameResetButton)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setGeometry(QRect(547, 0, 25, 25))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonReset.sizePolicy().hasHeightForWidth())
        self.pushButtonReset.setSizePolicy(sizePolicy1)
        self.pushButtonReset.setMinimumSize(QSize(25, 25))
        self.pushButtonReset.setMaximumSize(QSize(25, 25))
        self.pushButtonReset.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/retoolFiles/images/icons8-restart-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonReset.setIcon(icon1)
        self.pushButtonReset.setAutoDefault(False)
        self.labelContribute = QLabel(self.frameResetButton)
        self.labelContribute.setObjectName(u"labelContribute")
        self.labelContribute.setGeometry(QRect(0, 0, 381, 18))
        self.labelContribute.setMinimumSize(QSize(0, 18))
        self.labelContribute.setMaximumSize(QSize(16777215, 18))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        self.labelContribute.setFont(font4)
        self.labelContribute.setScaledContents(False)
        self.labelContribute.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelContribute.setWordWrap(True)
        self.labelContribute.setOpenExternalLinks(True)
        self.labelContribute.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.gridLayout.addWidget(self.frameResetButton, 0, 0, 1, 1)

        self.frameMetadataLocation = QFrame(self.gridLayoutWidget)
        self.frameMetadataLocation.setObjectName(u"frameMetadataLocation")
        self.frameMetadataLocation.setMinimumSize(QSize(0, 41))
        self.frameMetadataLocation.setMaximumSize(QSize(16777215, 41))
        self.frameMetadataLocation.setFrameShape(QFrame.StyledPanel)
        self.frameMetadataLocation.setFrameShadow(QFrame.Raised)
        self.buttonChooseMetadataLocation = QPushButton(self.frameMetadataLocation)
        self.buttonChooseMetadataLocation.setObjectName(u"buttonChooseMetadataLocation")
        self.buttonChooseMetadataLocation.setGeometry(QRect(0, 0, 41, 41))
        self.buttonChooseMetadataLocation.setFont(font1)
        self.buttonChooseMetadataLocation.setIcon(icon)
        self.buttonChooseMetadataLocation.setIconSize(QSize(32, 32))
        self.buttonChooseMetadataLocation.setAutoDefault(False)
        self.labelSelectMetadataLocation = QLabel(self.frameMetadataLocation)
        self.labelSelectMetadataLocation.setObjectName(u"labelSelectMetadataLocation")
        self.labelSelectMetadataLocation.setGeometry(QRect(50, 0, 531, 22))
        self.labelSelectMetadataLocation.setFont(font)
        self.labelMetadataLocation = QLabel(self.frameMetadataLocation)
        self.labelMetadataLocation.setObjectName(u"labelMetadataLocation")
        self.labelMetadataLocation.setGeometry(QRect(50, 20, 531, 20))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        self.labelMetadataLocation.setPalette(palette3)
        self.labelMetadataLocation.setFont(font2)

        self.gridLayout.addWidget(self.frameMetadataLocation, 4, 0, 1, 1)

        self.frameCloneListMetadataDownloadLocation = QFrame(self.gridLayoutWidget)
        self.frameCloneListMetadataDownloadLocation.setObjectName(u"frameCloneListMetadataDownloadLocation")
        self.frameCloneListMetadataDownloadLocation.setMinimumSize(QSize(0, 24))
        self.frameCloneListMetadataDownloadLocation.setMaximumSize(QSize(16777215, 24))
        self.frameCloneListMetadataDownloadLocation.setFrameShape(QFrame.StyledPanel)
        self.frameCloneListMetadataDownloadLocation.setFrameShadow(QFrame.Raised)
        self.lineEditCloneListDownloadLocation = QLineEdit(self.frameCloneListMetadataDownloadLocation)
        self.lineEditCloneListDownloadLocation.setObjectName(u"lineEditCloneListDownloadLocation")
        self.lineEditCloneListDownloadLocation.setGeometry(QRect(0, 0, 571, 24))
        self.lineEditCloneListDownloadLocation.setMinimumSize(QSize(0, 24))
        self.lineEditCloneListDownloadLocation.setMaximumSize(QSize(16777215, 24))

        self.gridLayout.addWidget(self.frameCloneListMetadataDownloadLocation, 9, 0, 1, 1)

        self.labelURLError = QLabel(Settings)
        self.labelURLError.setObjectName(u"labelURLError")
        self.labelURLError.setGeometry(QRect(15, 320, 571, 18))
        self.labelURLError.setMinimumSize(QSize(0, 18))
        self.labelURLError.setMaximumSize(QSize(16777215, 18))
        palette4 = QPalette()
        brush4 = QBrush(QColor(255, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.labelURLError.setPalette(palette4)

        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.labelCloneListMetadataDownloadURL.setText(QCoreApplication.translate("Settings", u"Clone list and metadata download URL", None))
#if QT_CONFIG(tooltip)
        self.buttonChooseCloneListsLocation.setToolTip(QCoreApplication.translate("Settings", u"Choose where the clone list folder is located", None))
#endif // QT_CONFIG(tooltip)
        self.buttonChooseCloneListsLocation.setText("")
        self.labelSelectCloneListsLocation.setText(QCoreApplication.translate("Settings", u"Clone list folder location", None))
        self.labelCloneListsLocation.setText(QCoreApplication.translate("Settings", u"No clone list folder selected", None))
        self.labelPaths.setText(QCoreApplication.translate("Settings", u"Paths", None))
        self.labelDownloadLocations.setText(QCoreApplication.translate("Settings", u"Download locations", None))
#if QT_CONFIG(tooltip)
        self.pushButtonReset.setToolTip(QCoreApplication.translate("Settings", u"Reset all settings to default", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonReset.setText("")
        self.labelContribute.setText(QCoreApplication.translate("Settings", u"<html><head/><body><p>Settings are saved automatically.</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.buttonChooseMetadataLocation.setToolTip(QCoreApplication.translate("Settings", u"Choose where the metadata folder is located", None))
#endif // QT_CONFIG(tooltip)
        self.buttonChooseMetadataLocation.setText("")
        self.labelSelectMetadataLocation.setText(QCoreApplication.translate("Settings", u"Metadata folder location", None))
        self.labelMetadataLocation.setText(QCoreApplication.translate("Settings", u"No metadata folder selected", None))
        self.labelURLError.setText(QCoreApplication.translate("Settings", u"URL isn't valid", None))
    # retranslateUi

