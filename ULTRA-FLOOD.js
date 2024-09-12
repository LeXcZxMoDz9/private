const { spawn } = require('child_process');

function runFloodScript(args) {
    const process = spawn('/root/private/node', ['hybrid.js', ...args]);

    process.stdout.on('data', (data) => {
        console.log(`Output: ${data}`);
    });

    process.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });

    process.on('close', (code) => {
        console.log(`Process exited with code ${code}. Restarting...`);
        runFloodScript(args);
    });
}

// Ambil argumen dari command line, abaikan 'node' dan nama script 'autoRestart.js'
const args = process.argv.slice(2);

runFloodScript(args);
