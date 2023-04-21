import QtQuick
import QtQuick.Controls
import QtQuick.Window

ApplicationWindow {
    id: window
    width: 360
    height: 200
    visible: true
    title: qsTr("Bless")

    QtObject {
        id: internal
        function quranWindowSwitch() {
            var component = Qt.createComponent("../../dquran/qml/main.qml");
            var win = component.createObject();
            win.show();
            visible = false;
        }
    }

    Label {
        id: blessQuranLabel
        height: 100
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
        text: "Bless Qur'an"
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        font.pointSize: 20
    }

    Button {
        id: startButton
        height: 100
        anchors {
            left: parent.left
            leftMargin: 5
            right: parent.right
            rightMargin: 5
            bottom: parent.bottom
            bottomMargin: 5
        }
        text: "Start"
        onClicked: {
            internal.quranWindowSwitch();
        }
    }
}
