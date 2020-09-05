import os,pyshark

class RTP_Audio:
    def __init__ (self,inp_file,out_file,filter):
        self.input = inp_file
        self.output = out_file
        self.filter = filter

    def to_audio (self):
        print(self.filter)
        rtp_list = []
        input_pyshark = pyshark.FileCapture(self.input,display_filter=self.filter)
        with open (self.output,'wb') as f:
            for x in range (100):
                print(x)
                rtp_val = input_pyshark[x][3]
                rtp_list.append(rtp_val.payload.split(':'))

            for x in rtp_list:
                packet = " ".join(x)
                res_audio = bytearray.fromhex(packet)
                f.write(res_audio)

        print('DONE')

audio = RTP_Audio('input_file.pcap','output.raw','rtp').to_audio()
