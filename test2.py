import os,pyshark


class RTP_Audio:
    def __init__ (self,inp_file,out_file,filter):
        self.input = inp_file
        self.output = out_file
        self.filter = filter

    def to_audio (self):
        input_pyshark = pyshark.FileCapture(self.input,display_filter=self.filter)
        print(input_pyshark)
        # with open(self.output,'wb') as f:
        #     f.
        # res_audio = open(self.output,'wb')
        #
        # print(self.input)


audio = RTP_Audio('input_file.pcap','output','rtp').to_audio()
