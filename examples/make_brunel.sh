nvcc -ccbin=mpicc --compiler-options -Wall -arch sm_30 --ptxas-options=-v --maxrregcount=55 --relocatable-device-code true -L ../lib -I ../src -o ../bin/brunel brunel.cu -lm -lstdc++ -lneuralgpu

