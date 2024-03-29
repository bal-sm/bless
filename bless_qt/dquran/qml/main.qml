import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Window
import md.ayatproperties

ApplicationWindow {
    id: window
    minimumWidth: 540
    height: 70
    visible: true
    title: qsTr("Qur'an")

    Bridge {
        id: bridge
    }

    Popup {
        id: settingsPopup
        anchors.centerIn: parent
        width: 500
        height: 200
        modal: true
        focus: true
        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent

        onClosed: {
            window.height = row1.height + ayats.height + 7;
            window.minimumHeight = row1.height + ayats.height + 7;
            window.maximumHeight = row1.height + ayats.height + 7;
        }

        ColumnLayout {
            id: columnLayoutInSettingsPopup
            Label {
                id: settingsLabel
                Layout.alignment: Qt.AlignLeft
                text: "Settings"
            }

            RowLayout {
                Label {
                    id: fontSizeSliderLabel
                    Layout.alignment: Qt.AlignLeft
                    text: "Font size"
                }

                Slider {
                    id: fontSizeSlider
                    Layout.alignment: Qt.AlignRight
                    value: 0.5
                    onValueChanged: {
                        ayats.font.pointSize = bridge.getSize(fontSizeSlider.value);
                        console.log("`fontSizeSlider` `onValueChanged` `ayats.height` = " + ayats.height);
                        console.log("`fontSizeSlider` `onValueChanged` `quranScrollView.height` = " + quranScrollView.height);
                    }
                    Component.onCompleted: {
                        fontSizeSlider.value = bridge.returnSliderValueFromConfig(0);
                        console.log("`fontSizeSlider` `Component.onCompleted` `fontSizeSlider.value` = " + fontSizeSlider.value);
                    }
                }
            }
        }
    }

    ColumnLayout {
        id: columnLayout1
        anchors.fill: parent

        Row {
            id: row1
            Layout.alignment: Qt.AlignRight
            Button {
                id: settingButton
                Layout.fillWidth: true
                text: "Settings"
                onClicked: {
                    window.height = 300;
                    window.minimumHeight = 300;
                    window.maximumHeight = 300;
                    settingsPopup.open();
                }
            }
            ComboBox {
                id: suratComboBox
                width: 200
                model: suratModel
                onActivated: {
                    ayats.text = bridge.getAyatsForSurat(currentText);
                    console.log("`suratComboBox` `onActivated` `currentText` = " + currentText);
                }
            }
        }

        ScrollView {
            id: quranScrollView
            Layout.alignment: Qt.AlignTop
            Layout.fillHeight: true
            Layout.fillWidth: true

            Label {
                id: ayats
                text: "Loading"
                Component.onCompleted: {
                    ayats.font.pointSize = bridge.getSize(0);
                    ayats.text = bridge.getAyatsForSurat(suratComboBox.currentText);
                    quranScrollBarHorizontal.position = (1.0 - quranScrollBarHorizontal.size);
                    console.log("`ayats` `Component.onCompleted` `columnLayout1.height` = " + columnLayout1.height);
                    window.height = row1.height + ayats.height + 7;
                    window.width = bridge.getLastWindowWidth();
                    window.minimumHeight = row1.height + ayats.height + 7;
                    window.maximumHeight = row1.height + ayats.height + 7;
                    console.log("`Label` `Component.onCompleted` `row1.height` = " + row1.height);
                    console.log("`Label` `Component.onCompleted` `settingButton.height` = " + settingButton.height);
                    console.log("`Label` `Component.onCompleted` `quranScrollView.height` = " + quranScrollView.height);
                }
            }

            ScrollBar.horizontal: ScrollBar {
                id: quranScrollBarHorizontal
                anchors.left: quranScrollView.left
                anchors.right: quranScrollView.right
                anchors.bottom: quranScrollView.bottom
            }
        }
    }
    onClosing: {
        bridge.saveLastWindowWidth(window.width);
    }
}
// Actually let's keep using Qt for Python to honor Aa Greg Dawson saw., sayang muah.
