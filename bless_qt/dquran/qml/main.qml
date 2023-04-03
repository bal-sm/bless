import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Window

ApplicationWindow {
    id: window
    width: 540
    height: 70
    visible: true
    title: qsTr("Qur'an")

    Component {
        id: ayatDelegate

        Rectangle {
            id: wrapper
            height: anAyat.contentHeight
            width: anAyat.contentWidth

            Text {
                id: anAyat
                text: model.ayatinqt
                font.pointSize: 16
                horizontalAlignment: Text.AlignRight
            }
        }
    }

    Popup {
        id: popup
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
            Text {
                color: "black"
                Layout.alignment: Qt.AlignLeft
                text: "Settings"
            }

            RowLayout {
                Text {
                    id: rightlabel
                    color: "black"
                    Layout.alignment: Qt.AlignLeft
                    text: "Placeholder"
                }

                Slider {
                    id: slider
                    Layout.alignment: Qt.AlignRight
                    value: 0.5
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
                    popup.open();
                }
            }
            ComboBox {
                width: 200
                model: suratModel
            }
        }

        ScrollView {
            id: quranScrollView
            Layout.alignment: Qt.AlignTop
            Layout.fillHeight: true
            Layout.fillWidth: true

            Flickable {
                Label {
                    text: "yang panjanggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
                }
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
