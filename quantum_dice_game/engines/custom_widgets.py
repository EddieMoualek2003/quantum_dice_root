from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QEvent, QTimer, QVariantAnimation, Qt
from PyQt5.QtGui import QPainter, QLinearGradient, QColor, QBrush

class AnimatedGradientButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setText(text)
        self.setMinimumHeight(40)
        self.offset = 0
        self.hovered = False
        self.opacity = 0.0  # opacity from 0 to 1

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)

        self.fade_anim = QVariantAnimation()
        self.fade_anim.setDuration(500)
        self.fade_anim.setStartValue(0.0)
        self.fade_anim.setEndValue(1.0)
        self.fade_anim.valueChanged.connect(self.set_opacity)

        self.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                border: none;
                border-radius: 8px;
                color: white;
            }
        """)
        self.installEventFilter(self)

    def set_opacity(self, val):
        self.opacity = val
        self.update()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            self.hovered = True
            self.fade_anim.setDirection(QVariantAnimation.Forward)
            self.fade_anim.start()
            self.timer.start(50)  # slower rotation
        elif event.type() == QEvent.Leave:
            self.hovered = False
            self.fade_anim.setDirection(QVariantAnimation.Backward)
            self.fade_anim.start()
            self.timer.stop()
        return super().eventFilter(obj, event)

    def animate(self):
        self.offset = (self.offset + 3) % 360  # slow rotation
        self.update()

    def paintEvent(self, event):
        if self.opacity > 0.01:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            rect = self.rect()

            gradient = QLinearGradient(0, 0, rect.width(), 0)
            for i in range(7):
                hue = (self.offset + i * 50) % 360
                color = QColor.fromHsv(hue, 128, 200)
                color.setAlphaF(self.opacity)  # fade in/out
                gradient.setColorAt(i / 6, color)

            painter.setBrush(QBrush(gradient))
            painter.setPen(Qt.NoPen)
            painter.drawRoundedRect(rect, 8, 8)

            # Draw text
            painter.setPen(QColor(255, 255, 255, int(self.opacity * 255)))
            painter.drawText(rect, Qt.AlignCenter, self.text())
        else:
            super().paintEvent(event)
