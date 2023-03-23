import QtQuick
import QtQuick.Controls
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

    ListView {
        id: quransView
        anchors.fill: parent
        model: quranmodel
        orientation: Qt.Horizontal
        layoutDirection: Qt.RightToLeft

        delegate: ayatDelegate
    }
}
