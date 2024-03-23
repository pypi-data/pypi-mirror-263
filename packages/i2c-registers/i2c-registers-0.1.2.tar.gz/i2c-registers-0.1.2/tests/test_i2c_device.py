import unittest

from i2c_registers import *


class I2cDeviceTestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.section = I2cRegisterSection("test_seg", 0, 7, [0] * 8)
        self.register = I2cRegister("test_reg", 0x03,
                                    RegisterOperations.ReadWrite, False, {"test": self.section})

        self.device = I2cDevice(0x62, "big", None, {"test_reg": self.register})

    def test_properties(self):
        self.assertEqual(0x62, self.device.dev_addr)
        self.assertEqual("big", self.device.byte_order)
        self.assertEqual(None, self.device.i2c)

    def test_get(self):
        register = self.device.get("test_reg")
        self.assertEqual(0x03, register.reg_addr)
        return


if __name__ == '__main__':
    unittest.main()
