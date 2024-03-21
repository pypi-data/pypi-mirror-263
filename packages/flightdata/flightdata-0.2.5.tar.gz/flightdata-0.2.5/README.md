## FlightData
This repo is contains a set of datastructures and tools for handling flight log data.

### Flight 
The Flight object represents the data logged by a flight controller. The class wraps a pandas dataframe which is indexed on a single time axis. Where data is logged at different rates for different sensors it is mapped to the closest time index. Attribute access provides individual columns or sets of columns in the groups defined in Fields. Item access subsets the data in the time axis. 


### Table
The Table is the base type for most of the datastructures. It allows attribute access to individual columns. Attribute access is also available to return basic entities subclassed from the base type in the pfc-geometry package. For example in the state object table.x provides the x position, table.pos provides a Point representing the xyz position. columns that are not represented by geometric base types are considered to be labels for the data.

### State
The State object is a table representing the position and orientation of the aircraft along with their derivatives, it can be constructed from a Flight or from scratch by extrapolating in lines or around arcs. Many tools are provided to manipulate the data. The position and attitude are in a reference frame (with Z up), the derivatives move with the aircraft in either the body, wind, stability or track (like the wind axis but with no wind) frame.  



### Ardupilot DataFlash log Parameters:

for reference (pulled from ardupilot github https://github.com/dronekit/ardupilot-releases/blob/master/libraries/DataFlash/DataFlash.h):

LOG_BASE_STRUCTURES:

FMT       Type,Length,Name,Format,Columns

PARM      TimeUS,Name,Value

GPS       TimeUS,Status,GMS,GWk,NSats,HDop,Lat,Lng,RAlt,Alt,Spd,GCrs,VZ,U

GPS2      TimeUS,Status,GMS,GWk,NSats,HDop,Lat,Lng,RAlt,Alt,Spd,GCrs,VZ,U

GPA       TimeUS,VDop,HAcc,VAcc,SAcc

GPA2      TimeUS,VDop,HAcc,VAcc,SAcc

IMU       TimeUS,GyrX,GyrY,GyrZ,AccX,AccY,AccZ,ErrG,ErrA,Temp,GyHlt,AcHlt

MSG       TimeUS

RCIN      TimeUS,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14

RCOU      TimeUS,Ch1,Ch2,Ch3,Ch4,Ch5,Ch6,Ch7,Ch8,Ch9,Ch10,Ch11,Ch12

RSSI      TimeUS,RXRSSI

BARO      TimeUS,Alt,Press,Temp,CRt

POWR      TimeUS,Vcc,VServo,Flags

CMD       TimeUS,CTot,CNum,CId,Prm1,Prm2,Prm3,Prm4,Lat,Lng,Alt

RAD       TimeUS,RSSI,RemRSSI,TxBuf,Noise,RemNoise,RxErrors,Fixed

CAM       TimeUS,GPSTime,GPSWeek,Lat,Lng,Alt,RelAlt,Roll,Pitch,Yaw

ARSP      TimeUS,Airspeed,DiffPress,Temp,RawPress,Offset

CURR      TimeUS,Throttle,Volt,Curr,Vcc,CurrTot,Volt2

ATT       TimeUS,DesRoll,Roll,DesPitch,Pitch,DesYaw,Yaw,ErrRP,ErrYaw

MAG       TimeUS,MagX,MagY,MagZ,OfsX,OfsY,OfsZ,MOfsX,MOfsY,MOfsZ,Health

MODE      TimeUS,Mode,ModeNum

RFND      TimeUS,Dist1,Dist2,Dist3,Dist4

IMU2        TimeUS,GyrX,GyrY,GyrZ,AccX,AccY,AccZ,ErrG,ErrA,Temp,GyHlt, AcHlt 

IMU3        TimeUS,GyrX,GyrY,GyrZ,AccX,AccY,AccZ,ErrG,ErrA,Temp,GyHlt,AcHlt 

AHR2        TimeUS,Roll,Pitch,Yaw,Alt,Lat,Lng 

POS         TimeUS,Lat,Lng,Alt,RelAlt 

SIM         TimeUS,Roll,Pitch,Yaw,Alt,Lat,Lng 

EKF1        TimeUS,Roll,Pitch,Yaw,VN,VE,VD,PN,PE,PD,GX,GY,GZ 

EKF2        TimeUS,Ratio,AZ1bias,AZ2bias,VWN,VWE,MN,ME,MD,MX,MY,MZ 

EKF3        TimeUS,IVN,IVE,IVD,IPN,IPE,IPD,IMX,IMY,IMZ,IVT 

EKF4        TimeUS,SV,SP,SH,SMX,SMY,SMZ,SVT,OFN,EFE,FS,TS,SS 

TERR        TimeUS,Status,Lat,Lng,Spacing,TerrH,CHeight,Pending,Loaded 

UBX1        TimeUS,Instance,noisePerMS,jamInd,aPower,agcCnt 

UBX2        TimeUS,Instance,ofsI,magI,ofsQ,magQ 

UBX3        TimeUS,Instance,hAcc,vAcc,sAcc 

GRAW        TimeUS,WkMS,Week,numSV,sv,cpMes,prMes,doMes,mesQI,cno,lli 

GRXH        TimeUS,rcvTime,week,leapS,numMeas,recStat 

GRXS        TimeUS,prMes,cpMes,doMes,gnss,sv,freq,lock,cno,prD,cpD,doD,trk 

SBFE        TimeUS,TOW,WN,Mode,Err,Lat,Long,Height,Undul,Vn,Ve,Vu,COG 

ESC1        TimeUS,RPM,Volt,Curr,Temp 

ESC2        TimeUS,RPM,Volt,Curr,Temp 

ESC3        TimeUS,RPM,Volt,Curr,Temp 

ESC4        TimeUS,RPM,Volt,Curr,Temp 

ESC5        TimeUS,RPM,Volt,Curr,Temp 

ESC6        TimeUS,RPM,Volt,Curr,Temp 

ESC7        TimeUS,RPM,Volt,Curr,Temp 

ESC8        TimeUS,RPM,Volt,Curr,Temp 

EKF5        TimeUS,normInnov,FIX,FIY,AFI,HAGL,offset,RI,meaRng,errHAGL 

MAG2        TimeUS,MagX,MagY,MagZ,OfsX,OfsY,OfsZ,MOfsX,MOfsY,MOfsZ,Health 

MAG3        TimeUS,MagX,MagY,MagZ,OfsX,OfsY,OfsZ,MOfsX,MOfsY,MOfsZ,Health 

ACC1        TimeUS,SampleUS,AccX,AccY,AccZ 

ACC2        TimeUS,SampleUS,AccX,AccY,AccZ 

ACC3        TimeUS,SampleUS,AccX,AccY,AccZ 

GYR1        TimeUS,SampleUS,GyrX,GyrY,GyrZ 

GYR2        TimeUS,SampleUS,GyrX,GyrY,GyrZ 

GYR3        TimeUS,SampleUS,GyrX,GyrY,GyrZ 

PIDR        TimeUS,Des,P,I,D,FF,AFF 

PIDP        TimeUS,Des,P,I,D,FF,AFF 

PIDY        TimeUS,Des,P,I,D,FF,AFF 

PIDA        TimeUS,Des,P,I,D,FF,AFF 

PIDS        TimeUS,Des,P,I,D,FF,AFF 

BAR2        TimeUS,Alt,Press,Temp,CRt 

BAR3        TimeUS,Alt,Press,Temp,CRt 

VIBE        TimeUS,VibeX,VibeY,VibeZ,Clip0,Clip1,Clip2 

IMT         TimeUS,DelT,DelvT,DelAX,DelAY,DelAZ,DelVX,DelVY,DelVZ 

IMT2        TimeUS,DelT,DelvT,DelAX,DelAY,DelAZ,DelVX,DelVY,DelVZ 

IMT3        TimeUS,DelT,DelvT,DelAX,DelAY,DelAZ,DelVX,DelVY,DelVZ 

ORGN        TimeUS,Type,Lat,Lng,Alt 

RPM         TimeUS,rpm1,rpm2