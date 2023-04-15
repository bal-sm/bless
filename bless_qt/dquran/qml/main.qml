import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Window
import md.ayatproperties

ApplicationWindow {
    id: window
    width: 540
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
            window.width = 540;
            window.height = 70;
        }

        ColumnLayout {
            id: columnLayoutInSettingsPopup
            Label {
                id: settingsLabel
                color: "black"
                Layout.alignment: Qt.AlignLeft
                text: "Settings"
            }

            RowLayout {
                Text {
                    id: fontSizeSliderLabel
                    color: "black"
                    Layout.alignment: Qt.AlignLeft
                    text: "Font size"
                }

                Slider {
                    id: fontSizeSlider
                    Layout.alignment: Qt.AlignRight
                    value: 0.5
                    onValueChanged: {
                        ayats.font.pointSize = bridge.getSize(fontSizeSlider.value);
                    }
                    Component.onCompleted: {
                        fontSizeSlider.value = bridge.returnSliderValueFromConfig(0);
                        console.log(fontSizeSlider.value);
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
                    settingsPopup.open();
                }
            }
            ComboBox {
                id: suratComboBox
                width: 200
                model: suratModel
                onActivated: {
                    ayats.text = bridge.getAyatsForSurat(currentText);
                    console.log(currentText);
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
}
// Actually let's keep using Qt for Python to honor Aa Greg Dawson saw., sayang muah.
