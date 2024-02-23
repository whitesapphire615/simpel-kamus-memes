meme_dict = {"CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan,tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah",
            
}
            
word = input("Ketik kata yang tidak Kamu mengerti : ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('kata sepertinya tidak ada dikamus')
    
