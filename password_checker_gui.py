# ============================================================
#  Password Strength Checker — PyQt5 GUI
#  DecodeLabs Industrial Training Kit — Project 1
# ============================================================

import sys
import hmac
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QFrame, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

COMMON_PASSWORDS = {
    "password", "123456", "qwerty", "abc123", "letmein",
    "iloveyou", "admin", "welcome", "monkey", "dragon",
    "111111", "123456789", "password1", "sunshine", "master"
}

def check_password_strength(password: str) -> dict:
    has_length = len(password) >= 8
    has_upper  = any(c.isupper() for c in password)
    has_digit  = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    is_common = any(
        hmac.compare_digest(password.lower(), p) for p in COMMON_PASSWORDS
    )

    extra_score = sum([has_upper, has_digit, has_symbol])

    if is_common or not has_length:
        strength = "Weak"
    elif extra_score <= 2:
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "strength"  : strength,
        "has_length": has_length,
        "has_upper" : has_upper,
        "has_digit" : has_digit,
        "has_symbol": has_symbol,
        "is_common" : is_common,
    }


class CriterionRow(QWidget):
    def __init__(self, label: str):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 2, 0, 2)

        self.icon = QLabel("✘")
        self.icon.setFixedWidth(22)
        self.icon.setFont(QFont("Segoe UI", 11))

        self.text = QLabel(label)
        self.text.setFont(QFont("Segoe UI", 10))

        layout.addWidget(self.icon)
        layout.addWidget(self.text)
        layout.addStretch()
        self.set_state(False)

    def set_state(self, passed: bool):
        if passed:
            self.icon.setText("✔")
            self.icon.setStyleSheet("color: #4CAF50;")
            self.text.setStyleSheet("color: #4CAF50;")
        else:
            self.icon.setText("✘")
            self.icon.setStyleSheet("color: #888;")
            self.text.setStyleSheet("color: #888;")


class PasswordChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Strength Checker — DecodeLabs")
        self.setFixedSize(460, 500)
        self._visible = False
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2e;
                color: #cdd6f4;
                font-family: 'Segoe UI';
            }
            QLineEdit {
                background-color: #313244;
                color: #cdd6f4;
                border: 1px solid #45475a;
                border-radius: 8px;
                padding: 10px 14px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #89b4fa;
            }
            QPushButton#toggleBtn {
                background-color: #45475a;
                color: #cdd6f4;
                border: none;
                border-radius: 8px;
                padding: 10px 16px;
                font-size: 13px;
            }
            QPushButton#toggleBtn:hover {
                background-color: #585b70;
            }
            QFrame#card {
                background-color: #313244;
                border-radius: 10px;
            }
            QLabel#title {
                font-size: 18px;
                font-weight: bold;
                color: #cdd6f4;
            }
            QLabel#sublabel {
                font-size: 11px;
                color: #6c7086;
            }
        """)
        self._build_ui()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 28, 28, 28)
        root.setSpacing(16)

        # Title
        title = QLabel("🔐 Password Strength Checker")
        title.setObjectName("title")
        root.addWidget(title)

        sub = QLabel("DecodeLabs Industrial Training Kit — Project 1")
        sub.setObjectName("sublabel")
        root.addWidget(sub)

        # Input + toggle button side by side
        input_row = QHBoxLayout()
        input_row.setSpacing(8)

        self.pw_input = QLineEdit()
        self.pw_input.setPlaceholderText("Enter a password...")
        self.pw_input.setEchoMode(QLineEdit.Password)
        self.pw_input.textChanged.connect(self._on_change)

        self.toggle_btn = QPushButton("Show")
        self.toggle_btn.setObjectName("toggleBtn")
        self.toggle_btn.setFixedWidth(60)
        self.toggle_btn.setCursor(Qt.PointingHandCursor)
        self.toggle_btn.clicked.connect(self._toggle_visibility)

        input_row.addWidget(self.pw_input)
        input_row.addWidget(self.toggle_btn)
        root.addLayout(input_row)

        # Strength bar
        self.bar_bg = QFrame()
        self.bar_bg.setFixedHeight(8)
        self.bar_bg.setStyleSheet("background:#313244; border-radius:4px;")
        root.addWidget(self.bar_bg)

        self.bar_fill = QFrame(self.bar_bg)
        self.bar_fill.setFixedHeight(8)
        self.bar_fill.setStyleSheet("background:#45475a; border-radius:4px;")
        self.bar_fill.setFixedWidth(0)

        # Strength label
        self.strength_label = QLabel("Start typing...")
        self.strength_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.strength_label.setStyleSheet("color: #6c7086;")
        root.addWidget(self.strength_label)

        # Criteria card
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(16, 14, 16, 14)
        card_layout.setSpacing(6)

        card_title = QLabel("Criteria")
        card_title.setFont(QFont("Segoe UI", 10, QFont.Bold))
        card_title.setStyleSheet("color: #89b4fa;")
        card_layout.addWidget(card_title)

        self.c_length = CriterionRow("At least 8 characters")
        self.c_upper  = CriterionRow("Uppercase letter [A-Z]")
        self.c_digit  = CriterionRow("Contains a digit [0-9]")
        self.c_symbol = CriterionRow("Contains a symbol [!@#$...]")

        for w in [self.c_length, self.c_upper, self.c_digit, self.c_symbol]:
            card_layout.addWidget(w)

        root.addWidget(card)

        # Verdict
        self.verdict = QLabel("")
        self.verdict.setWordWrap(True)
        self.verdict.setFont(QFont("Segoe UI", 10))
        self.verdict.setStyleSheet("""
            padding: 10px 14px;
            border-radius: 8px;
            background: #313244;
            color: #6c7086;
        """)
        self.verdict.hide()
        root.addWidget(self.verdict)

        root.addStretch()

    def _toggle_visibility(self):
        self._visible = not self._visible
        self.pw_input.setEchoMode(
            QLineEdit.Normal if self._visible else QLineEdit.Password
        )
        self.toggle_btn.setText("Hide" if self._visible else "Show")

    def _on_change(self, text: str):
        if not text:
            self.strength_label.setText("Start typing...")
            self.strength_label.setStyleSheet("color: #6c7086;")
            self.bar_fill.setFixedWidth(0)
            for w in [self.c_length, self.c_upper, self.c_digit, self.c_symbol]:
                w.set_state(False)
            self.verdict.hide()
            return

        r = check_password_strength(text)

        self.c_length.set_state(r["has_length"])
        self.c_upper.set_state(r["has_upper"])
        self.c_digit.set_state(r["has_digit"])
        self.c_symbol.set_state(r["has_symbol"])

        cfg = {
            "Weak"  : ("#f38ba8", 120, "Too weak. Increase length and add more character types."),
            "Medium": ("#fab387", 260, "Getting there! Add more character variety."),
            "Strong": ("#a6e3a1", 404, "Strong password. All criteria met — great work!"),
        }
        color, bar_w, tip = cfg[r["strength"]]

        self.strength_label.setText(r["strength"])
        self.strength_label.setStyleSheet(f"color: {color};")
        self.bar_fill.setStyleSheet(f"background:{color}; border-radius:4px;")
        self.bar_fill.setFixedWidth(bar_w)

        if r["is_common"]:
            tip = "⚠ Found in leaked password lists! Choose something unique."
            color = "#f38ba8"

        self.verdict.setText(tip)
        self.verdict.setStyleSheet(f"""
            padding: 10px 14px;
            border-radius: 8px;
            background: #313244;
            color: {color};
            border-left: 3px solid {color};
        """)
        self.verdict.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PasswordChecker()
    window.show()
    sys.exit(app.exec_())