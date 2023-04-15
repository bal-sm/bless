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
        id: columnLayout2
        anchors.fill: parent

        Row {
            Layout.alignment: Qt.AlignRight
            Button {
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
                // onClicked: {
                //     ayats.text = bridge.getAyatsForSurat(yangDiKlikDiComboBoxKumahaNya)
                // }
                // "bukan onClicked, sayang." - Allah swt. and Muhammad saw.
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
                // text: bridge.getAyatsForSurat("An-Nās")
                // TypeError: Cannot call method 'getAyatsForSurat' of null
                Component.onCompleted: {
                    ayats.font.pointSize = bridge.getSize(0);
                    ayats.text = bridge.getAyatsForSurat(suratComboBox.currentText);
                    ayatsScrollBarHorizontal.position = (1.0 - ayatsScrollBarHorizontal.size);
                }
            }

            ScrollBar.horizontal: ScrollBar {
                id: ayatsScrollBarHorizontal
                anchors.left: quranScrollView.left
                anchors.right: quranScrollView.right
                anchors.bottom: quranScrollView.bottom
            }
            // ListView {
            //     // bener pake ListView
            //     model: quranmodel
            //     orientation: Qt.Horizontal
            //     layoutDirection: Qt.RightToLeft

            //     // Ayat highlighter pake rectangle thing tea.anAyat
            //     // value dari ListView teh nanti yang
            //     // word per ayat nanti di Django nya pake model per word nya id={1 2 3 4 5} nanti nulisnya mau meninggal pusing mikirnya, terus nanti modelnya string berupa 4 (alif) 1 (lam) 2 (ra') aja nanti ini mah, di surga. belajar unicode caranya kenapa bisa gitu.)
            //     delegate: ayatDelegate
            // }
        }
    }
}
// Carbon heueuh, python the best buat pemula, and quick coding, Rust the best.
