# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: EnvolventeCompleja SSB
# Author: J&V
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal







class EnvolventeComplejaSSB(gr.hier_block2):
    def __init__(self, Ac=1, K=1):
        gr.hier_block2.__init__(
            self, "EnvolventeCompleja SSB",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Ac = Ac
        self.K = K

        ##################################################
        # Blocks
        ##################################################
        self.hilbert_fc_0 = filter.hilbert_fc(257, window.WIN_HAMMING, 6.76)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(Ac)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(K)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self, 0))
        self.connect((self.hilbert_fc_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self, 0), (self.hilbert_fc_0, 0))


    def get_Ac(self):
        return self.Ac

    def set_Ac(self, Ac):
        self.Ac = Ac
        self.blocks_multiply_const_vxx_1.set_k(self.Ac)

    def get_K(self):
        return self.K

    def set_K(self, K):
        self.K = K
        self.blocks_multiply_const_vxx_0.set_k(self.K)

