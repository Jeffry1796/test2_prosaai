import pyshark

def to_audio(name_file,filter1):
    join_rtp = []
    input_pyshark = pyshark.FileCapture(name_file,display_filter=filter1)

    for i in range (1000):
        try:
            rtp_val = input_pyshark[i][3]
            if rtp_val.payload:
                join_rtp.append("".join(rtp_val.payload.split(':')))
        except:
            pass
        
    rtp_packet = "".join(join_rtp)

    return rtp_packet
