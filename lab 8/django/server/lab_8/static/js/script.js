class TableUser{
    constructor(){
        console.log(2)
        this.data = []
        this.init(this)
        this.setBtn()
        
    }

    async init(self){
        $.ajax({
            url: '/static/json/data_users.json', 
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                self.data = response
                self.load()
                const select = document.querySelector('select')
                select.addEventListener('change', () => self.load(select.value))
            }
        })
    }

    start(){
        document.getElementById('table').innerHTML = ''
        document.getElementById('blockBtn').innerHTML = ''
    }

    load(index = 3){
        this.start()
        this.getBtn(index)
        let i = 0
        let n = this.num
        let y = index + this.num
        console.log(this.data[this.num])
        for(; i < index; i++){
            if(n < y)
                this.loadBlock(this.data[n])
            n++
        }
    }

    getBtn(index){
        let i = 1
        let btnIndex = this.data[this.data.length - 1].id / index
        if (this.data[this.data.length - 1].id % index != 0)
            btnIndex++
        do{
            const btn = document.createElement('button')
            btn.textContent = i
            btn.classList = 'offBtn'
            btn.id = index * (i - 1)
            btn.addEventListener('click', () => {
                this.setBtn(index, btn.id)
            })
            document.getElementById('blockBtn').appendChild(btn)
            i++
        }while(i <= btnIndex)
    }

    setBtn(index = 3, element = 0){
        this.num = Number(element)
        this.load(index)
    }

    loadBlock(item){
        document.getElementById('table').insertAdjacentHTML('beforeend', `
        <tr>
            <td>${item.id}</td>
            <td>${item.name}</td>
            <td>${item.title}</td>
            <td>${item.rase__race}</td>
            <td>${item.profession__profession}</td>
            <td>${item.level}</td>
            <td>${item.birthday}</td>
            <td>${item.banned}</td>
        </tr>
        `)
    }
}

document.addEventListener('DOMContentLoaded', () => new TableUser())