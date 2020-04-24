# DP_python
- Position detector app, communication with STM32F407G board via VCP

- Software part of myDiploma thesis
- software works in Correlation/RMS mode
	-Correlation mode: - user can set carry frequency (of genereated signal - internal) that the input signal is correlated with
					- user can also set the distance that changes phase shift of internally generated signal

	-RMS mode: STM board will switch to RMS calculation - no internal signal is needed therefore none is generated
	
	- spot calibration : - Spot calibration always scale down - for example: If your X width if laser spot is twice larger then Y,
																then the function will virtualy scale down X -> coord changes in X and Y are same
- dev. note : pyinstall --onefile -w -i logo_2.ico
