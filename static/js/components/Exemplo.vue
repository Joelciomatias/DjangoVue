<template>
    <div id="">
        <table class="table">
        <thead>
            <th>Titulo</th>
            <th>Plataforma</th>
        </thead>
        <tbody>
            
            <tr v-for="game in lista" :key="game.id"> 
                <td>{{ game.fields.titulo }}</td>
                <td>{{ game.fields.plataformas }}</td>
            </tr>
            
        </tbody>
    </table>

    </div>
</template>
<script>
export default {
    
    data() {
        return{
            lista:[]
        }
    },
    mounted(){
        this.$http.get("homepage/games").then((req
        ) => this.lista = req.data)

    }
}
</script>
<style lang="css">

</style>


