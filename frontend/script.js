console.log('loaded')

document.querySelectorAll('button[data-op]').forEach(button => {
    button.onclick = async () => {
        const op = button.dataset.op;
        const a = document.getElementById('a').value;
        const b = document.getElementById('b').value;

        try {
            const res = await fetch(`https://calculator-app-t9i1.onrender.com/calculate/${op}?a=${a}&b=${b}`);
            const data = await res.json();
            document.getElementById('result').textContent = data.result;

        } catch (err) {
            console.error(err);
        }
    }
})