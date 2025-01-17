# Autogenerated with SMOP version 0.23
# main.py ../../assessing-mininet/MATLAB/load_function.m ../../assessing-mininet/MATLAB/process_complete_test_set.m ../../assessing-mininet/MATLAB/process_single_testfile.m ../../assessing-mininet/MATLAB/ProcessAllLogsMain.m

from __future__ import division
from numpy import arange
def strcat(*args):
    return ''.join(args)
def load_octave_decoded_file_as_matrix(file_name):
    with open(file_name, 'r') as f:
        return [ map(float,line.strip().split(' ')) for line in f ]

def get_test_bitrate(crosstraffic):
    if crosstraffic:
        return arange(4,6,0.25)
    else:
        return arange(8,12,0.5)

def process_complete_test_set(file_names,output_format,crosstraffic):
    from glob import glob

    overview_img_file=strcat('overview.',output_format)
    mean_bitrate=[]
    std_dev_bitrate=[]
    mean_delay=[]
    std_dev_delay=[]
    mean_jitter=[]
    std_dev_jitter=[]
    mean_packetloss=[]
    std_dev_packetloss=[]
    print('Starting work on:')
    print(file_names)
    for f in file_names:
        print('in loop, iterating through list of found files...')
        #current_file_name_with_ext=f
        #bare_file_name=strrep(current_file_name_with_ext,extension_loadfile,'')
        #temp_picture_file_name=strcat(bare_file_name,extension_imgfile)
        current_picture_file_name=strcat(f,'.jpg')
        matrix_to_process=load_octave_decoded_file_as_matrix(f)
        parsed_data=process_single_testfile(matrix_to_process,current_picture_file_name,output_format)
        mean_bitrate[ii]=mean(parsed_data)
        std_dev_bitrate[ii]=std(parsed_data)
        mean_delay[ii]=mean(parsed_data[:,2])
        std_dev_delay[ii]=std(parsed_data[:,2])
        mean_jitter[ii]=mean(parsed_data[:,3])
        std_dev_jitter[ii]=std(parsed_data[:,3])
        mean_packetloss[ii]=mean(parsed_data[:,4])
        std_dev_packetloss[ii]=std(parsed_data[:,4])

    bitrate_of_test = get_test_bitrate(crosstraffic)
    s_bitrate=min(bitrate_of_test) - bitrate_interval
    e_bitrate=max(bitrate_of_test) + bitrate_interval
    s_mean_bitrate=min(mean_bitrate) - max(std_dev_bitrate)
    e_mean_bitrate=max(mean_bitrate) + max(std_dev_bitrate)
    s_mean_jitter=min(mean_jitter) - max(std_dev_jitter)
    e_mean_jitter=max(mean_jitter) + max(std_dev_jitter)
    s_mean_delay=min(mean_delay) - max(std_dev_delay)
    e_mean_delay=max(mean_delay) + max(std_dev_delay)
    axis_bitrate=(cat(s_bitrate,e_bitrate,s_mean_bitrate,e_mean_bitrate))
    axis_delay=(cat(s_bitrate,e_bitrate,sort(cat(round_(s_mean_delay) - 1,round_(e_mean_delay) + 1))))
    axis_jitter=(cat(s_bitrate,e_bitrate,s_mean_jitter,e_mean_jitter))
    print('\n\n\n*** START TESTDATA ***\n')
    print(bitrate_of_test)
    print(mean_bitrate)
    print(std_dev_bitrate)
    print('\n*** END TESTDATA ***\n\n\n')
    subplot(3,1,1)
    print(len(bitrate_of_test))
    print(len(mean_bitrate))
    print(len(std_dev_bitrate))
    errorbar(bitrate_of_test,mean_bitrate,std_dev_bitrate,'kx')
    title('mean throughput with standard deviation')
    xlabel('test bitrate [Mbps]')
    ylabel('bitrate value [Mbps]')
    print(axis_bitrate)
    axis(axis_bitrate)
    grid('on')
    subplot(3,1,2)
    errorbar(bitrate_of_test,mean_delay,std_dev_delay,'kx')
    title('mean delay with standard deviation')
    xlabel('test bitrate [Mbps]')
    ylabel('delay value [ms]')
    axis(axis_delay)
    grid('on')
    subplot(3,1,3)
    errorbar(bitrate_of_test,mean_jitter,std_dev_jitter,'kx')
    title('mean jitter with standard deviation')
    xlabel('test bitrate [Mbps]')
    ylabel('jitter value [ms]')
    axis(axis_jitter)
    grid('on')
    aggregatedPicture=figure(1)
    set_(aggregatedPicture,'PaperUnits','centimeters')
    set_(aggregatedPicture,'PaperSize',cat(30,16))
    set_(aggregatedPicture,'PaperPosition',cat(0,0,30,16))
    set_(aggregatedPicture,'PaperOrientation','portrait')
    saveas(aggregatedPicture,overview_img_file,output_format)
    close(aggregatedPicture)
    clear('all')
    return
def process_single_testfile(matrix,current_picture_file_name,output_format):
    t_start=matrix[1][5] * 3600 + matrix[1][6] * 60 + matrix[1][7]
    print (matrix[:][5] * 3600 + matrix[:][6] * 60 + matrix[:][7])
    t_conv=(matrix[:][5] * 3600 + matrix[:][6] * 60 + matrix[:][7]) - t_start
    t_start_s=matrix[1][2] * 3600 + matrix[1][3] * 60 + matrix[1][4]
    t_conv_s=(matrix[:][2] * 3600 + matrix[:][3] * 60 + matrix[:][4]) - t_start_s
    jj=1
    t_int=0
    bitrate[jj]=0
    delay[jj]=0
    jitter[jj]=0
    pktloss[jj]=0
    for ii in arange(1,len(matrix)).reshape(-1):
        if (t_conv[ii] - t_int >= 1):
            jj=jj + 1
            t_int=t_conv[ii]
            bitrate[jj]=matrix[ii][8]
            delay[jj]=t_conv[ii] - t_conv_s[ii]
            if (ii > 1):
                pktloss[jj]=matrix[ii] - matrix[ii - 1] - 1
                jitter[jj]=t_conv[ii] - t_conv[ii - 1]
        else:
            bitrate[jj]=bitrate[jj] + matrix[ii][8]
            delay[jj]=mean(cat(delay[jj],(t_conv[ii] - t_conv_s[ii])))
            if (ii > 1):
                pktloss[jj]=pktloss[jj] + matrix[ii] - matrix[ii - 1] - 1
                jitter[jj]=mean(cat(jitter[jj],(t_conv[ii] - t_conv[ii - 1])))
    bitrate=bitrate / 125000
    return_matrix=matlabarray(cat(bitrate.T,delay.T,jitter.T,pktloss.T))
    subplot(2,2,1)
    bitrate_u=copy(bitrate)
    plot(arange(0,jj - 2),bitrate_u[1:jj - 1],'-')
    title('Throughput')
    xlabel('time [s]')
    ylabel('[Mbps]')
    axis(cat(0,max(t_conv),0,round_(max(bitrate_u) * 1.125)))
    grid('on')
    subplot(2,2,2)
    plot(arange(0,len(delay) - 1),delay,'-')
    title('Delay')
    xlabel('time [s]')
    ylabel('[ms]')
    axis(cat(0,max(t_conv),min(delay) - 1e-05,max(delay)))
    grid('on')
    subplot(2,2,3)
    plot(arange(0,len(jitter) - 1),jitter,'-')
    title('Jitter')
    xlabel('time [s]')
    ylabel('[ms]')
    axis(cat(0,max(t_conv),min(jitter) - max(jitter) * 1.125,max(jitter) * 1.125))
    grid('on')
    subplot(2,2,4)
    d=diff(t_conv)
    m=max(d)
    hist(d)
    title('Inter-departure time Distribution')
    xlabel('time [s]')
    ylabel('Empirical PDF')
    grid('on')
    firstPicture=figure(1)
    set_(firstPicture,'PaperUnits','centimeters')
    set_(firstPicture,'PaperSize',cat(22,18))
    set_(firstPicture,'PaperPosition',cat(0,0,22,18))
    set_(firstPicture,'PaperOrientation','portrait')
    saveas(firstPicture,current_picture_file_name,output_format)
    close(firstPicture)
    # if (strcmp(log_type,'udp_rcv')):
    #     subplot(1,1,1)
    #     packetloss_picture=figure(1)
    #     set_(packetloss_picture,'PaperUnits','centimeters')
    #     set_(packetloss_picture,'PaperSize',cat(12,10))
    #     set_(packetloss_picture,'PaperPosition',cat(0,0,12,10))
    #     set_(packetloss_picture,'PaperOrientation','portrait')
    #     plot(arange(0,len(pktloss) - 1),pktloss,'-')
    #     title('Packet loss')
    #     xlabel('time [s]')
    #     ylabel('[pps]')
    #     axis(cat(sort(cat(0,max(t_conv))),sort(cat(round_(max(pktloss)) + 1,round_(min(pktloss)) - 1))))
    #     grid('on')
    #     saveas(packetloss_picture,strcat('pl_',current_picture_file_name),output_format)
    #     close(packetloss_picture)
    return return_matrix
crosstraffic = False
#process_complete_test_set(['/tmp/octave.dat'],'pdf',crosstraffic)
process_single_testfile(load_octave_decoded_file_as_matrix('/tmp/octave.dat'),'pic.jpg',"jpg")
