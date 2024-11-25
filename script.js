document.getElementById('upload-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('file');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('http://127.0.0.1:5000', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('output').textContent = JSON.stringify(result, null, 2);
});
