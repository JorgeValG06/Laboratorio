# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ModuladorAM_J1B
# Author: Jorge_Valeria
# Copyright: UIS
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal







class ModuladorAM_J1B(gr.hier_block2):
    def __init__(self, Ac=1, ka=1):
        gr.hier_block2.__init__(
            self, "ModuladorAM_J1B",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ac = Ac
        self.ka = ka

        ##################################################
        # Blocks
        ##################################################
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(Ac)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(ka)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_0, 0))


    def get_Ac(self):
        return self.Ac

    def set_Ac(self, Ac):
        self.Ac = Ac
        self.blocks_multiply_const_vxx_1.set_k(self.Ac)

    def get_ka(self):
        return self.ka

    def set_ka(self, ka):
        self.ka = ka
        self.blocks_multiply_const_vxx_0.set_k(self.ka)

