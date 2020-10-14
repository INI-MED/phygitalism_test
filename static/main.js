 fetch("/api/meta")
     .then(response => response.json())
     .then(json => {
        const { data } = json;

        for (const item of data) {
            const block = document.createElement('div');
            block.classList.add('list-item');
            const fileName = document.createElement('div');
            const fileType = document.createElement('div');
            const fileTime = document.createElement('div');
            fileName.textContent = item.name;
            fileType.textContent = item.type;
            fileTime.textContent = item.time;
            block.appendChild(fileName);
            block.appendChild(fileType);
            block.appendChild(fileTime);
            document.body.appendChild(block);
        }
     })
     .catch(({ data }) => console.error('Error: ', data));