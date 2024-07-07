const http = require('http');
const { exec } = require('child_process');

const server = http.createServer((req, res) => {
    if (req.url === '/clear') {
        // Execute clear command
        exec('clear', (error, stdout, stderr) => {
            if (error) {
                console.error(`exec error: ${error}`);
                res.writeHead(500, {'Content-Type': 'text/plain'});
                res.end('Failed to execute clear command');
                return;
            }
            console.log(`stdout: ${stdout}`);
            console.error(`stderr: ${stderr}`);
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.end('Clear command executed successfully');
        });
    } else {
        res.writeHead(404, {'Content-Type': 'text/plain'});
        res.end('Not found');
    }
});

const port = 3000;
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});
