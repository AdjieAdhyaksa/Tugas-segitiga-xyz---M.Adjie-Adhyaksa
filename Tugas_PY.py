def Segitiga(x: int, y: int, z: int) -> str:
  
  """
  Args:
    x (int): Panjang sisi pertama segitiga.
    y (int): Panjang sisi kedua segitiga.
    z (int): Panjang sisi ketiga segitiga.

  Returns:
    str: Jenis segitiga ("sama sisi", "sama kaki", atau "sembarang").
  """

  if x == y == z:
    return "Segitiga sama sisi"
  elif x == y or x == z or y == z:
    return "Segitiga sama kaki"
  else:
    return "Segitiga sembarang"

while True:
  
  sisi_a = int(input("Masukkan nilai x: "))
  sisi_b = int(input("Masukkan nilai y: "))
  sisi_c = int(input("Masukkan nilai z: "))

  Sisi = Segitiga(sisi_a, sisi_b, sisi_c)

  print(f"Jenis segitiga: {Sisi}")

  lagi = input("Repeat? (y/t): ")
  if lagi.lower() != "y":
    break