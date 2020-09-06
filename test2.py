import os,pyshark
import argparse

class RTP_Audio:
    def __init__ (self,inp_file,out_file,filter1):
        self.input = inp_file
        self.output = out_file
        self.filter = filter1

    def to_audio (self):
        print(self.filter)
        rtp_list = []
        input_pyshark = pyshark.FileCapture(self.input,display_filter=self.filter)
        with open (self.output,'wb') as f:
            
            for i in range (1000):
                try:
                    print(i)
                    rtp_val = input_pyshark[i][3]
                    if rtp_val.payload:
                        rtp_list.append(rtp_val.payload.split(':'))
                except:
                    pass

            for rtp_f in rtp_list:  
                packet = " ".join(rtp_f)         
                res_audio = bytearray.fromhex(packet)
                f.write(res_audio)

        print('DONE')

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,help="path to input file")
ap.add_argument("-o", "--output", required=True,help="path to output image")
args = ap.parse_args()
audio = RTP_Audio(args.input,args.output,'rtp').to_audio()
