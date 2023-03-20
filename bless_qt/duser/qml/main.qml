import QtQuick
import QtQuick.Controls
import QtQuick.Window


ApplicationWindow{
    id: window
    width: 360
    height: 200
    visible: true
    title: qsTr("Bless")

    QtObject{
        id: internal
        function quranWindowSwitch() {
            var component = Qt.createComponent("../../dquran/qml/main.qml")
            var win = component.createObject()
            win.show()
            visible = false
        }
    }
    
    Button{
        id: startButton
        anchors.fill: parent
        text: "Start"
        onClicked: {
            internal.quranWindowSwitch()
        }
    }
}
