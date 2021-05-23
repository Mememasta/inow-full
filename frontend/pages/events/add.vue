<template>
    <div>
        <br>
        <div class="container">
            <h4> Создание мероприятия </h4>
        </div>
        <br>

        <div class="container">

        <form @submit.prevent="createEvent">

            <div class="form-group">
            <label for="inputName">Название мероприятия</label>
            <input type="text" name='name' v-model="name" class="form-control" id="inputName" placeholder="Название мероприятия" required>
            </div>

            <div class="form-group">
            <label for="inputDescription">Описание мероприятия</label>
            <textarea type="text" name='description' v-model="description" class="form-control" id="inputDescription" placeholder="Описание мероприятия" required></textarea>
            </div>

            <p>
                <label for="date">Дата: </label>
                <br>
                <input type="date" id="date" name="event_date" v-model="date" required />
            </p>
            <p>
                <label for="date">Время: </label>
                <br>
                <input type="time" id="date" name="event_date" v-model="time" required />
            </p>

            <input type="submit" class="btn btn-primary" value="Добавить мероприятие" />

        </form>

        </div>
        <br>
    </div>
</template>

<script>
export default {
    layout: "MainLayout",
    head: {
        title: 'Создание мероприятия',
    },
    data() {
        return {
            name: '',
            description: '',
            date: '',
            time: '',
            errors: []
        }
    },
    methods: {
        async createEvent() {
            await this.$axios
            .post("/event/create", {
                name: this.name,
                description: this.description,
                event_date: this.date + 'T' + this.time,
                photo_path: "@assets/img/football.jpg"
            })
            .then(response => {
                this.$router.push({ path: "/events" });
            })
            .catch(e => {
                this.errors.push(e)
            })
        }
    }
}
</script>
