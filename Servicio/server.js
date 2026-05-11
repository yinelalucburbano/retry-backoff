const express = require('express');
const app = express();
const PORT = 3000;

app.get('/data', (req, res) => {
    const shouldFail = Math.random() < 0.7; // 70% de probabilidad de fallo

    if (shouldFail) {
        console.log("Generando error 500 intencional...");
        res.status(500).send('Error Interno del Servidor');
    } else {
        console.log("Solicitud exitosa enviada!");
        res.status(200).json({ message: "¡Éxito! Datos recuperados." });
    }
});

app.listen(PORT, () => {
    console.log(`Servidor de error corriendo en http://localhost:${PORT}`);
});