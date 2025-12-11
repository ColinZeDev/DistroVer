import QtQuick.Controls
import QtQuick.Layouts
import QtQuick

ApplicationWindow {
    id: win
    width: 659
    height: 515
    visible: true
    title: "DistroVer v" + backend.version

    minimumWidth: 659
    maximumWidth: 659
    minimumHeight: 515
    maximumHeight: 515

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 20
        spacing: 20

        Image {
            id: logo
            source: backend.logo
            fillMode: Image.PreserveAspectFit
            width: 160
            height: 160
            Layout.alignment: Qt.AlignHCenter
        }

        Rectangle {
            height: 1
            color: "#555"
            Layout.fillWidth: true
        }

        Text {
            id: info
            text: backend.infoText
            font.pixelSize: 14
            wrapMode: Text.Wrap
            color: "black"
            horizontalAlignment: Text.AlignHCenter
            Layout.alignment: Qt.AlignHCenter
            Layout.fillWidth: true
        }

        /*
        Button {
            text: "DistroVer Source Code"
            Layout.alignment: Qt.AlignHCenter

            onClicked: {
                Qt.openUrlExternally("https://github.com/ColinZeDev/DistroVer")
            }
        }
        */
    }

    background: Rectangle { color: "#ffffff" }
}