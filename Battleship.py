#!/usr/bin/env python3

import time
A11 = ["  ", "A11", "  "]
A12 = ["  ", "A12", "  "]
A13 = ["  ", "A13", "  "]
A14 = ["  ", "A14", "  "]
A15 = ["  ", "A15", "  "]
A16 = ["  ", "A16", "  "]
A17 = ["  ", "A17", "  "]
A18 = ["  ", "A18", "  "]
A19 = ["  ", "A19", "  "]
A110 = ["  ", "A110", "  "]
B11 = ["  ", "B11", "  "]
B12 = ["  ", "B12", "  "]
B13 = ["  ", "B13", "  "]
B14 = ["  ", "B14", "  "]
B15 = ["  ", "B15", "  "]
B16 = ["  ", "B16", "  "]
B17 = ["  ", "B17", "  "]
B18 = ["  ", "B18", "  "]
B19 = ["  ", "B19", "  "]
B110 = ["  ", "B110", "  "]
C11 = ["  ", "C11", "  "]
C12 = ["  ", "C12", "  "]
C13 = ["  ", "C13", "  "]
C14 = ["  ", "C14", "  "]
C15 = ["  ", "C15", "  "]
C16 = ["  ", "C16", "  "]
C17 = ["  ", "C17", "  "]
C18 = ["  ", "C18", "  "]
C19 = ["  ", "C19", "  "]
C110 = ["  ", "C110", "  "]
D11 = ["  ", "D11", "  "]
D12 = ["  ", "D12", "  "]
D13 = ["  ", "D13", "  "]
D14 = ["  ", "D14", "  "]
D15 = ["  ", "D15", "  "]
D16 = ["  ", "D16", "  "]
D17 = ["  ", "D17", "  "]
D18 = ["  ", "D18", "  "]
D19 = ["  ", "D19", "  "]
D110 = ["  ", "D110", "  "]
E11 = ["  ", "E11", "  "]
E12 = ["  ", "E12", "  "]
E13 = ["  ", "E13", "  "]
E14 = ["  ", "E14", "  "]
E15 = ["  ", "E15", "  "]
E16 = ["  ", "E16", "  "]
E17 = ["  ", "E17", "  "]
E18 = ["  ", "E18", "  "]
E19 = ["  ", "E19", "  "]
E110 = ["  ", "E110", "  "]
F11 = ["  ", "F11", "  "]
F12 = ["  ", "F12", "  "]
F13 = ["  ", "F13", "  "]
F14 = ["  ", "F14", "  "]
F15 = ["  ", "F15", "  "]
F16 = ["  ", "F16", "  "]
F17 = ["  ", "F17", "  "]
F18 = ["  ", "F18", "  "]
F19 = ["  ", "F19", "  "]
F110 = ["  ", "F110", "  "]
G11 = ["  ", "G11", "  "]
G12 = ["  ", "G12", "  "]
G13 = ["  ", "G13", "  "]
G14 = ["  ", "G14", "  "]
G15 = ["  ", "G15", "  "]
G16 = ["  ", "G16", "  "]
G17 = ["  ", "G17", "  "]
G18 = ["  ", "G18", "  "]
G19 = ["  ", "G19", "  "]
G110 = ["  ", "G110", "  "]
H11 = ["  ", "H11", "  "]
H12 = ["  ", "H12", "  "]
H13 = ["  ", "H13", "  "]
H14 = ["  ", "H14", "  "]
H15 = ["  ", "H15", "  "]
H16 = ["  ", "H16", "  "]
H17 = ["  ", "H17", "  "]
H18 = ["  ", "H18", "  "]
H19 = ["  ", "H19", "  "]
H110 = ["  ", "H110", "  "]
I11 = ["  ", "I11", "  "]
I12 = ["  ", "I12", "  "]
I13 = ["  ", "I13", "  "]
I14 = ["  ", "I14", "  "]
I15 = ["  ", "I15", "  "]
I16 = ["  ", "I16", "  "]
I17 = ["  ", "I17", "  "]
I18 = ["  ", "I18", "  "]
I19 = ["  ", "I19", "  "]
I110 = ["  ", "I110", "  "]
J11 = ["  ", "J11", "  "]
J12 = ["  ", "J12", "  "]
J13 = ["  ", "J13", "  "]
J14 = ["  ", "J14", "  "]
J15 = ["  ", "J15", "  "]
J16 = ["  ", "J16", "  "]
J17 = ["  ", "J17", "  "]
J18 = ["  ", "J18", "  "]
J19 = ["  ", "J19", "  "]
J110 = ["  ", "J110", "  "]

A21 = ["  ", "A21", "  "]
A22 = ["  ", "A22", "  "]
A23 = ["  ", "A23", "  "]
A24 = ["  ", "A24", "  "]
A25 = ["  ", "A25", "  "]
A26 = ["  ", "A26", "  "]
A27 = ["  ", "A27", "  "]
A28 = ["  ", "A28", "  "]
A29 = ["  ", "A29", "  "]
A210 = ["  ", "A210", "  "]
B21 = ["  ", "B21", "  "]
B22 = ["  ", "B22", "  "]
B23 = ["  ", "B23", "  "]
B24 = ["  ", "B24", "  "]
B25 = ["  ", "B25", "  "]
B26 = ["  ", "B26", "  "]
B27 = ["  ", "B27", "  "]
B28 = ["  ", "B28", "  "]
B29 = ["  ", "B29", "  "]
B210 = ["  ", "B210", "  "]
C21 = ["  ", "C21", "  "]
C22 = ["  ", "C22", "  "]
C23 = ["  ", "C23", "  "]
C24 = ["  ", "C24", "  "]
C25 = ["  ", "C25", "  "]
C26 = ["  ", "C26", "  "]
C27 = ["  ", "C27", "  "]
C28 = ["  ", "C28", "  "]
C29 = ["  ", "C29", "  "]
C210 = ["  ", "C210", "  "]
D21 = ["  ", "D21", "  "]
D22 = ["  ", "D22", "  "]
D23 = ["  ", "D23", "  "]
D24 = ["  ", "D24", "  "]
D25 = ["  ", "D25", "  "]
D26 = ["  ", "D26", "  "]
D27 = ["  ", "D27", "  "]
D28 = ["  ", "D28", "  "]
D29 = ["  ", "D29", "  "]
D210 = ["  ", "D210", "  "]
E21 = ["  ", "E21", "  "]
E22 = ["  ", "E22", "  "]
E23 = ["  ", "E23", "  "]
E24 = ["  ", "E24", "  "]
E25 = ["  ", "E25", "  "]
E26 = ["  ", "E26", "  "]
E27 = ["  ", "E27", "  "]
E28 = ["  ", "E28", "  "]
E29 = ["  ", "E29", "  "]
E210 = ["  ", "E210", "  "]
F21 = ["  ", "F21", "  "]
F22 = ["  ", "F22", "  "]
F23 = ["  ", "F23", "  "]
F24 = ["  ", "F24", "  "]
F25 = ["  ", "F25", "  "]
F26 = ["  ", "F26", "  "]
F27 = ["  ", "F27", "  "]
F28 = ["  ", "F28", "  "]
F29 = ["  ", "F29", "  "]
F210 = ["  ", "F210", "  "]
G21 = ["  ", "G21", "  "]
G22 = ["  ", "G22", "  "]
G23 = ["  ", "G23", "  "]
G24 = ["  ", "G24", "  "]
G25 = ["  ", "G25", "  "]
G26 = ["  ", "G26", "  "]
G27 = ["  ", "G27", "  "]
G28 = ["  ", "G28", "  "]
G29 = ["  ", "G29", "  "]
G210 = ["  ", "G210", "  "]
H21 = ["  ", "H21", "  "]
H22 = ["  ", "H22", "  "]
H23 = ["  ", "H23", "  "]
H24 = ["  ", "H24", "  "]
H25 = ["  ", "H25", "  "]
H26 = ["  ", "H26", "  "]
H27 = ["  ", "H27", "  "]
H28 = ["  ", "H28", "  "]
H29 = ["  ", "H29", "  "]
H210 = ["  ", "H210", "  "]
I21 = ["  ", "I21", "  "]
I22 = ["  ", "I22", "  "]
I23 = ["  ", "I23", "  "]
I24 = ["  ", "I24", "  "]
I25 = ["  ", "I25", "  "]
I26 = ["  ", "I26", "  "]
I27 = ["  ", "I27", "  "]
I28 = ["  ", "I28", "  "]
I29 = ["  ", "I29", "  "]
I210 = ["  ", "I210", "  "]
J21 = ["  ", "J21", "  "]
J22 = ["  ", "J22", "  "]
J23 = ["  ", "J23", "  "]
J24 = ["  ", "J24", "  "]
J25 = ["  ", "J25", "  "]
J26 = ["  ", "J26", "  "]
J27 = ["  ", "J27", "  "]
J28 = ["  ", "J28", "  "]
J29 = ["  ", "J29", "  "]
J210 = ["  ", "J210", "  "]


cuz = """
	   1      2      3      4      5      6      7      8      9      10
	 ______ ______ ______ ______ ______ ______ ______ ______ ______ ______
	|      |      |      |      |      |      |      |      |      |      |
 A  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______|
	|      |      |      |      |      |      |      |      |      |      |
 B  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______|
	|      |      |      |      |      |      |      |      |      |      |
 C  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______|
	|      |      |      |      |      |      |      |      |      |      |
 D  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______|
	|      |      |      |      |      |      |      |      |      |      |
 E  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______|
	|      |      |      |      |      |      |      |      |      |      |
 F  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______|
	|      |      |      |      |      |      |      |      |      |      |
 G  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______|
	|      |      |      |      |      |      |      |      |      |      |
 H  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______|
	|      |      |      |      |      |      |      |      |      |      |
 I  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______|
	|      |      |      |      |      |      |      |      |      |      |
 J  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |
	|______|______|______|______|______|______|______|______|______|______| """


board1 = [A11, A12, A13, A14, A15, A16, A17, A18, A19, B110, B11, B12, B13, B14, B15, B16, B17, B18, B19, B110, C11, C12, C13, C14, C15, C16, C17, C18, C19, C110, D11, D12, D13, D14, D15, D16, D17, D18, D19, D110, E11, E12, E13, E14, E15, E16, E17, E18, E19, E110, F11, F12, F13, F14, F15, F16, F17, F18, F19, F110, G11, G12, G13, G14, G15, G16, G17, G18, G19, G110, H11, H12, H13, H14, H15, H16, H17, H18, H19, H110, I11, I12, I13, I14, I15, I16, I17, I18, I19, I110, J11, J12, J13, J14, J15, J16, J17, J18, J19, J110]

board2 = [A21, A22, A23, A24, A25, A26, A27, A28, A29, B210, B21, B22, B23, B24, B25, B26, B27, B28, B29, B210, C21, C22, C23, C24, C25, C26, C27, C28, C29, C210, D21, D22, D23, D24, D25, D26, D27, D28, D29, D210, E21, E22, E23, E24, E25, E26, E27, E28, E29, E210, F21, F22, F23, F24, F25, F26, F27, F28, F29, F210, G21, G22, G23, G24, G25, G26, G27, G28, G29, G210, H21, H22, H23, H24, H25, H26, H27, H28, H29, H210, I21, I22, I23, I24, I25, I26, I27, I28, I29, I210, J21, J22, J23, J24, J25, J26, J27, J28, J29, J210]

def printboard(key, vis):
	if key == 1:
		if vis == 0:
			print("\nYour board:")
		elif p1[-1] == "s" or p1[-1] == "S":
			print("\n", p1, "' board:", sep="")
		else:
			print("\n", p1, "'s board:", sep="")
		print(
			"         1      2      3      4      5      6      7      8      9      10\n       ______ ______ ______ ______ ______ ______ ______ ______ ______ ______\n      |      |      |      |      |      |      |      |      |      |      |\n   A  | ",
			A11[vis], " | ", A12[vis], " | ", A13[vis], " | ", A14[vis], " | ", A15[vis], " | ", A16[vis], " | ", A17[vis], " | ", A18[vis], " | ", A19[vis], " | ", A110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   B  | ",
			B11[vis], " | ", B12[vis], " | ", B13[vis], " | ", B14[vis], " | ", B15[vis], " | ", B16[vis], " | ", B17[vis], " | ", B18[vis], " | ", B19[vis], " | ", B110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   C  | ",
			C11[vis], " | ", C12[vis], " | ", C13[vis], " | ", C14[vis], " | ", C15[vis], " | ", C16[vis], " | ", C17[vis], " | ", C18[vis], " | ", C19[vis], " | ", C110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   D  | ",
			D11[vis], " | ", D12[vis], " | ", D13[vis], " | ", D14[vis], " | ", D15[vis], " | ", D16[vis], " | ", D17[vis], " | ", D18[vis], " | ", D19[vis], " | ", D110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   E  | ",
			E11[vis], " | ", E12[vis], " | ", E13[vis], " | ", E14[vis], " | ", E15[vis], " | ", E16[vis], " | ", E17[vis], " | ", E18[vis], " | ", E19[vis], " | ", E110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   F  | ",
			F11[vis], " | ", F12[vis], " | ", F13[vis], " | ", F14[vis], " | ", F15[vis], " | ", F16[vis], " | ", F17[vis], " | ", F18[vis], " | ", F19[vis], " | ", F110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   G  | ",
			G11[vis], " | ", G12[vis], " | ", G13[vis], " | ", G14[vis], " | ", G15[vis], " | ", G16[vis], " | ", G17[vis], " | ", G18[vis], " | ", G19[vis], " | ", G110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   H  | ",
			H11[vis], " | ", H12[vis], " | ", H13[vis], " | ", H14[vis], " | ", H15[vis], " | ", H16[vis], " | ", H17[vis], " | ", H18[vis], " | ", H19[vis], " | ", H110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   I  | ",
			I11[vis], " | ", I12[vis], " | ", I13[vis], " | ", I14[vis], " | ", I15[vis], " | ", I16[vis], " | ", I17[vis], " | ", I18[vis], " | ", I19[vis], " | ", I110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   J  | ",
			J11[vis], " | ", J12[vis], " | ", J13[vis], " | ", J14[vis], " | ", J15[vis], " | ", J16[vis], " | ", J17[vis], " | ", J18[vis], " | ", J19[vis], " | ", J110[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|")
	elif key == 2:
		if vis == 0:
			print("\nYour board:")
		if p2[-1] == "s" or p2[-1] == "S":
			print("\n", p2, "' board:", sep="")
		else:
			print("\n", p2, "'s board:", sep="")
		print(
			"         1      2      3      4      5      6      7      8      9      10\n       ______ ______ ______ ______ ______ ______ ______ ______ ______ ______\n      |      |      |      |      |      |      |      |      |      |      |\n   A  | ",
			A21[vis], " | ", A22[vis], " | ", A23[vis], " | ", A24[vis], " | ", A25[vis], " | ", A26[vis], " | ", A27[vis], " | ", A28[vis], " | ", A29[vis], " | ", A210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   B  | ",
			B21[vis], " | ", B22[vis], " | ", B23[vis], " | ", B24[vis], " | ", B25[vis], " | ", B26[vis], " | ", B27[vis], " | ", B28[vis], " | ", B29[vis], " | ", B210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   C  | ",
			C21[vis], " | ", C22[vis], " | ", C23[vis], " | ", C24[vis], " | ", C25[vis], " | ", C26[vis], " | ", C27[vis], " | ", C28[vis], " | ", C29[vis], " | ", C210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   D  | ",
			D21[vis], " | ", D22[vis], " | ", D23[vis], " | ", D24[vis], " | ", D25[vis], " | ", D26[vis], " | ", D27[vis], " | ", D28[vis], " | ", D29[vis], " | ", D210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   E  | ",
			E21[vis], " | ", E22[vis], " | ", E23[vis], " | ", E24[vis], " | ", E25[vis], " | ", E26[vis], " | ", E27[vis], " | ", E28[vis], " | ", E29[vis], " | ", E210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   F  | ",
			F21[vis], " | ", F22[vis], " | ", F23[vis], " | ", F24[vis], " | ", F25[vis], " | ", F26[vis], " | ", F27[vis], " | ", F28[vis], " | ", F29[vis], " | ", F210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   G  | ",
			G21[vis], " | ", G22[vis], " | ", G23[vis], " | ", G24[vis], " | ", G25[vis], " | ", G26[vis], " | ", G27[vis], " | ", G28[vis], " | ", G29[vis], " | ", G210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   H  | ",
			H21[vis], " | ", H22[vis], " | ", H23[vis], " | ", H24[vis], " | ", H25[vis], " | ", H26[vis], " | ", H27[vis], " | ", H28[vis], " | ", H29[vis], " | ", H210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   I  | ",
			I21[vis], " | ", I22[vis], " | ", I23[vis], " | ", I24[vis], " | ", I25[vis], " | ", I26[vis], " | ", I27[vis], " | ", I28[vis], " | ", I29[vis], " | ", I210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|\n      |      |      |      |      |      |      |      |      |      |      |\n   J  | ",
			J21[vis], " | ", J22[vis], " | ", J23[vis], " | ", J24[vis], " | ", J25[vis], " | ", J26[vis], " | ", J27[vis], " | ", J28[vis], " | ", J29[vis], " | ", J210[vis],
			" |\n      |______|______|______|______|______|______|______|______|______|______|")


def check(player):
	if player == p1:
		for box in board1:
			if box in S11+S12+S13+S14+S15:
				box[0] = "██"
			else:
				box[0] = "  "

	if player == p2:
		for box in board2:
			if box in S21+S22+S23+S24+S25:
				box[0] = "██"
			else:
				box[0] = "  "

S11 = [A11, A12]
S12 = [C11, C12]
S13 = [E11, E12, E13]
S14 = [G11, G12, G13, G14]
S15 = [I11, I12, I13, I14, I15]

S21 = [A21, A22]
S22 = [C21, C22]
S23 = [E21, E22, E23]
S24 = [G21, G22, G23, G24]
S25 = [I21, I22, I23, I24, I25]

shipsp1 = [S11, S12, S13, S14, S15]
shipsp2 = [S21, S22, S23, S24, S25]


def roundis(player):
	i = 0
	did = 0
	while i == 0:
		printboard(1, 0)
		printboard(2, 2)
		print("\nHey", player, "it's your turn to blow 'em all!\n\nPress 'S' to shoot, 'M' to mark, 'P' to pass or 'G' to give up.")
		action = input().upper()

		if action == "S":
			if did == 1:
				print("You've already shot!")
			elif did == 0:
				printboard(2, 2)
				loc = input("Where do you want to shoot? (Example: F9)\n").upper()
				if len(loc) != 2 or loc[0] + "2" + loc[1] not in [item[1] for item in board2]:
					print("Please insert a valid location.")
					time.sleep(2)
				elif player == p1:
					for box in board2:
						if box[1] == loc[0] + "2" + loc[1]:
							if box[0] == "██":
								print("Yes! Got ya!")
								box[2] = "██"
								box[0] = "▓▓"
								did = 1
							elif box[2] == "██" or box[2] == "░░":
								print("You've already shot here!")
							elif box[0] == "  ":
								print("Ooops... You missed! Better luck next time.")
								box[2] = "░░"
								did = 1
							time.sleep(2)
				elif player == p2:
					for box in board1:
						if box[1] == loc[0] + "1" + loc[1]:
							if box[0] == "██":
								print("Yes! Got ya!")
								box[2] = "██"
								box[0] = "▓▓"
								did = 1
							elif box[2] == "██" or box[2] == "░░":
								print("You've already shot here!")
							elif box[0] == "  ":
								print("Ooops... You missed! Better luck next time.")
								box[2] = "░░"
								did = 1
							time.sleep(2)

		elif action == "M":
			loc = input("What do you want to mark?\n").upper()
			if len(loc) != 2 or loc[0] + "2" + loc[1] not in [item[1] for item in board2]:
				print("Please insert a valid location.")
				time.sleep(2)
			elif player == p1:
				for box in board2:
					if box[1] == loc[0] + "2" + loc[1]:
						if box[2] == "██" or box[2] == "░░":
							print("Ooops... Can't mark here.")
						elif box[2] == "  ":
							box[2] = "MM"
							print(loc, "marked!")
						time.sleep(2)
			elif player == p2:
				for box in board1:
					if box[1] == loc[0] + "2" + loc[1]:
						if box[2] == "██":
							print("Ooops... Can't mark here.")
						elif box[2] == "  ":
							box[2] = "MM"
							print(loc, "marked!")
						time.sleep(2)

		elif action == "G":
			print("I knew it!", player, "is a pussy!")
			exit()

		elif action == "P":
			if did == 0:
				print("You did nothing!")
			if did == 1:
				print("Bye then")
				i = 1

tut = input("Do you already know how to play? (y/n)\n").upper()

while tut == "N":
	input("Each player has five ships of five different sizes and gets to position them on the 10x10 board without letting the other see.\nPress 'Enter' to continue...\n")
	input("When it's your turn you can decide where to shoot at your enemy's board and the system is going to tell you wether you succeded or failed at aiming your opponent's ship and if the entire ship has drowned.\nPress 'Enter' to continue...\n")
	input("You are also able to mark areas on the board where you think the ships are so that you can keep track on your strategy.\nPress 'Enter' to continue...\n")

	tut = input("The game ends when all the ships of one player are lost.\nAre you ready to play? (y/n)\n").upper()

p1 = input("Player one, please type in your name: ")
while len(p1) > 10 or len(p1) < 3:
	p1 = input("Your name should be at least 3 and no more than 10 characters long: ")

p2 = input("Player two, please type in your name: ")
while len(p2) > 10 or len(p1) < 3:
	p2 = input("Also your name should be at least 3 and no more than 10 characters long, you fucking dumbass: ")

print(p2, ", look away!", sep="")
input("")

check(p1)
printboard(1, 0)
print("\n", p1, ", this is your board!", sep="")
input("I have randomly placed your five ships, but you can move and rotate each one of them as you'd like.\n")
ready = "N"
while ready == "N":
	check(p1)
	printboard(1, 0)
	print("\n\nSelect a ship to move (Example: 3)\n")
	num = int(input())-1
	movit = "Y"
	while movit == "Y":
		print("Where do you want to move ship number ", num+1, "? (Use WASD followed by Enter)\n", sep="")
		mov = input("").upper()
		if len(mov) > 1:
			mov = input("Please only type one direction\n").upper()
		for piece in shipsp1[num]:
			if mov == "W":
				if board1.index(shipsp1[num][0]) < 10:
					printboard(1, 0)
					print(shipsp1[num])
					mov = input("Can't go there!\n")
				shipsp1[num][shipsp1[num].index(piece)] = board1[board1.index(piece)-10]
				print(shipsp1[num])
			if mov == "S":
				if board1.index(shipsp1[num][-1]) > 90:
					printboard(1, 0)
					mov = input("Can't go there!\n")
				shipsp1[num][shipsp1[num].index(piece)] = board1[board1.index(piece)+10]
			if mov == "A":
				if board1.index(shipsp1[num][0]) == 1 or str(board1.index(shipsp1[0]))[1] == 1:
					printboard(1, 0)
					mov = input("Can't go there!\n")
				shipsp1[num][shipsp1[num].index(piece)] = board1[board1.index(piece)-1]
			if mov == "D":
				if len(str(board1.index(shipsp1[num][-1]))) == 2 and str(board1.index(shipsp1[num][-1]))[1] == "0":
					printboard(1, 0)
					mov = input("Can't go there!\n")
				shipsp1[num][shipsp1[num].index(piece)] = board1[board1.index(piece)+1]
		check(p1)
		printboard(1, 0)
		movit = input("\n\nDo you want to move it again? (y/n)\n")
	ready = input("Are you ready to play? (y/n)\n")

roundis(p1)
printboard(1, 0)
printboard(2, 2)
print(p1, ", look away!", sep="")
input("")
roundis(p2)
printboard(2, 0)
printboard(1, 2)
