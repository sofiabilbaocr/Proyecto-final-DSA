document.addEventListener('DOMContentLoaded', () => { //Espera a que la página esté lista antes de empezar a mover las cosas. Ocurre cuando el navegador termino de leer todo el documento
    loadLibrary();
    updateUI();
});

// Dibuja toda la UI
async function updateUI() {
    const res = await fetch('/status'); //Llama a el estado actual del array
    const data = await res.json();

    // Actualizar el texto del reproductor
    const currentSong = data.current_song; //Qué canción está sonando
    document.getElementById('current-song-title').innerText = currentSong ? `▶ ${currentSong}` : "Selecciona una canción"; //Si hay canción play si no aviso
    document.getElementById('stack-now-playing').innerText = currentSong ? `🎧 ${currentSong}` : "🎵 Selecciona una canción";
    
    document.getElementById('idx-prev').innerText = data.top1_index; //Escrine en html el valor del puntero de la izquierda
    document.getElementById('idx-next').innerText = data.top2_index;//Lo mismo pero de la derecha

    const stackViz = document.getElementById('stack-viz'); //Busca la barra (que dejamos vacía) para dibujar los 20 slots
    
    stackViz.innerHTML = data.raw_array.map((slot, i) => { //recorre todos los slots
        let type = "empty-zone";
        let icon = ""; //Cuadro vacío y sin nada por defecto

        // Zona isquierda, las canciones anteriores
        if (i <= data.top1_index) {
            type = "prev-zone";
            icon = "🎵";
        } 
        // Zona derecha, las canciones próximas
        else if (i >= data.top2_index) {
            type = "next-zone";
            icon = "🎵";
        }
        
        // La canción actual. la pintamos en el primer espacio disponible despues de la pila izquiera
        if (currentSong && i === (data.top1_index + 1) && i < data.top2_index) {
            type = "current-song"; 
            icon = "▶";
        }

        return `<div class="stack-slot ${type}">${icon}</div>`;
    }).join(''); }

// Carga las canciones de la base de datos
async function loadLibrary() {
    try {
        const res = await fetch('/api/library'); //Pide la lista a la api
        const songs = await res.json(); //Guarda los datos en un json dentro de la songs
        const container = document.getElementById('library-container'); //Busca el contenedor vacío que dejamos en el html

        container.innerHTML = songs.map(s => { //mapea las canciones y hace un pedazo de html para cada una
            const fullTitle = `${s.nombre} - ${s.artista}`; //Extrae el nombre de la canción y el artista 
            const escapedTitle = fullTitle.replace(/'/g, "\\'"); // Reemplazamos comillas simples en HTML para evitar errores si el nombre tiene comillas
            
            //Aquí se escribe el html gracias a esta comilla ` 
            return `
                <div class="song-card">
                    <strong>${s.nombre}</strong><br>
                    <small>${s.artista}</small><br>
                    <button onclick="addSong('${escapedTitle}')">
                        ➕ Agregar
                    </button>
                </div>
            `;
        }).join('');
    } catch (error) {
        console.error("Error cargando biblioteca:", error); //Error por si no carga la biblioteca
    }
}

async function addSong(songTitle) { //Damos una canción al backend para que lo agregue a la funcionalidad del double stack
    try {
        const response = await fetch('/add', {
            method: 'POST',
            headers: { //Avisa que se enviará algo en formato json
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ song: songTitle }), //El contenido del paquete
        });

        const result = await response.json();
        console.log("Respuesta del servidor:", result); //Respuesta para obtener más info en caso de errores

        updateUI();
    } catch (error) {
        console.error("Error en la petición fetch:", error); //Validación de error
    }
}

async function nextSong() {
    await fetch('/next', { method: 'POST' }); //Ejecuta la función next del api
    updateUI(); //Llama a update para vovler a dibujar el array actual
}

async function prevSong() {
    await fetch('/prev', { method: 'POST' }); //Ejecuta la función prev del api
    updateUI();
}

async function clearStack() {
    try {
        const response = await fetch('/clear', { method: 'POST' }); //Ejecuta la función clear del api para vaciar el array
        const result = await response.json();
        console.log("Stack vaciado:", result);
        updateUI(); //Llama a update para vovler a dibujar el array actual
    } catch (error) {
        console.error("Error vaciando el stack:", error);
    }
}