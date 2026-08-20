html_content = """<!DOCTYPE html>
<html lang="mg">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galerie Sary</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }
        h1 {
            text-align: center;
            color: white;
            font-size: 2.5rem;
            margin-bottom: 40px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 25px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .card {
            background: white;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
            text-align: center;
        }
        .card:hover {
            transform: translateY(-10px);
        }
        .card img {
            width: 100%;
            height: 250px;
            object-fit: contain;
            border-radius: 15px;
            background-color: #f8f9fa;
        }
        .card p {
            margin-top: 15px;
            font-size: 1.2rem;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>🎨 Galerie Sary</h1>
    <div class="gallery">
        <div class="card"><img src="boy.png" alt="Ankizilahy"><p>Ankizilahy</p></div>
        <div class="card"><img src="girl.png" alt="Ankizivavy"><p>Ankizivavy</p></div>
        <div class="card"><img src="panda.png" alt="Panda kely"><p>Panda kely</p></div>
        <div class="card"><img src="elephant.png" alt="Elefanta manga"><p>Elefanta manga</p></div>
        <div class="card"><img src="sun.png" alt="Masoandro"><p>Masoandro mitsiky</p></div>
        <div class="card"><img src="cat.png" alt="Saka kely"><p>Saka kely</p></div>
        <div class="card"><img src="plane.png" alt="Fiaramanidina"><p>Fiaramanidina</p></div>
        <div class="card"><img src="dog.png" alt="Alika kely"><p>Alika kely</p></div>
    </div>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("✅ Vita! Ny index.html dia voasoratra soa aman-tsara.")
