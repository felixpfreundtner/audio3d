import unittest
import gui_utils
import sys


class GuiTests(unittest.TestCase):
    """
    H1 -- GuiTests
    ************************
    **Test class for GUI.**
    Athor: Huijiang, Manuela
    """
    def setUp(self):
        self.state = gui_utils.State()

    def test_switch_stop_playback(self):
        """
        H2 -- test_switch_stop_playback
        ===================
        **This tests function switch_stop_playback() from gui_utils.**
        """
        sol = self.state.switch_stop_playback()
        error_msg = "test_switch_stop_playback failed!"
        self.assertEqual(sol, True, msg=error_msg)

    def test_switch_pause_playback(self):
        """
        H2 -- test_switch_pause_playback
        ===================
        **This tests function switch_pause_playback() from gui_utils.**
        """
        sol = self.state.switch_pause_playback()
        error_msg = "test_switch_pause_playback failed!"
        self.assertEqual(sol, True, msg=error_msg)

    def test_get_bound_pos_negative(self):
        """
        H2 -- test_get_bound_pos_negative
        ===================
        **This tests function get_bound_pos() from gui_utils for netative
        values.**
        """
        x = 350
        y = -30
        solx, soly = gui_utils.get_bound_pos(x, y)
        res_x = 350
        res_y = 0
        error_msg = "test_get_bound_pos_negative failed!"
        self.assertEqual(solx, res_x, msg=error_msg)
        self.assertEqual(soly, res_y, msg=error_msg)

    def test_get_bound_pos_float(self):
        """
        H2 -- test_get_bound_pos_float
        ===================
        **This tests function get_bound_pos() from gui_utils for float
        values.**
        """
        x = 370
        y = 0.0
        solx, soly = gui_utils.get_bound_pos(x, y)
        res_x = 350
        res_y = 0
        error_msg = "test_get_bound_pos_float failed!"
        self.assertEqual(solx, res_x, msg=error_msg)
        self.assertEqual(soly, res_y, msg=error_msg)

    def test_get_abs_pos_zero(self):
        """
        H2 -- test_get_abs_pos_zero
        ===================
        **This tests function get_abs_pos() from gui_utils for zero entries.**
        """
        res = [170, 170]
        solx, soly = self.state.get_abs_pos(90, 0)
        error_msg = "test_get_abs_pos_zero failed!"
        self.assertEqual(solx, res[0], msg=error_msg)
        self.assertEqual(soly, res[1], msg=error_msg)

    def test_get_abs_pos_float(self):
        """
        H2 -- test_get_abs_pos_float
        ===================
        **This tests function get_abs_pos() from gui_utils for floats.**
        """
        res = [170, 170]
        solx, soly = self.state.get_abs_pos(1.0, 0)
        error_msg = "test_get_abs_pos_float failed!"
        self.assertEqual(solx, res[0], msg=error_msg)
        self.assertEqual(soly, res[1], msg=error_msg)

    def test_get_abs_pos(self):
        """
        H2 -- test_get_abs_pos_float
        ===================
        **This tests function get_abs_pos() from gui_utils.**
        """
        res = [170, 270]
        solx, soly = self.state.get_abs_pos(180, 100)
        error_msg = "test_get_abs_pos failed!"
        self.assertEqual(solx, res[0], msg=error_msg)
        self.assertEqual(soly, res[1], msg=error_msg)


if __name__ == '__main__':
    app = gui_utils.QtGui.QApplication(sys.argv)
    unittest.main()
