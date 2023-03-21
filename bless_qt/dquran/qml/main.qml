import QtQuick
import QtQuick.Controls
import QtQuick.Window

ApplicationWindow {
    id: window
    width: 540
    height: 70
    visible: true
    title: qsTr("Qur'an")

    ScrollView {
        anchors.fill: parent

        ListView {
            id: quransView
            model: quranmodel
            orientation: Qt.Horizontal
            layoutDirection: Qt.RightToLeft

            delegate: Row {
                Text {
                    text: model.ayatinqt
                }
            }
        }
    }
}
