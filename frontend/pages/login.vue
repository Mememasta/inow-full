<template>
    <div
        class="card container form-signin text-center"
        style="width: 30em; border-radius: 15px"
    >
        <b-form @submit.prevent="onSubmit" @reset="onReset" v-if="show">
            <h1 class="h3 m-4 font-weight-normal">Вход</h1>

            <b-form-group id="email" label-for="email">
                <b-form-input
                    id="email"
                    v-model="form.username"
                    type="email"
                    required
                    placeholder="Введите email"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="password" label-for="password">
                <b-form-input
                    id="password"
                    v-model="form.password"
                    type="password"
                    required
                    placeholder="Введите пароль"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-4">
                <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
                    <b-form-checkbox value="me">Запомнить</b-form-checkbox>
                </b-form-checkbox-group>
            </b-form-group>

            <b-button type="submit" variant="primary" block>Войти</b-button>

            <br />

            <NuxtLink to="/signup">Регистрация</NuxtLink> |
            <NuxtLink to="/">Главная</NuxtLink>
            <p class="mt-3 mb-3 text-muted">&copy; 2021</p>
        </b-form>
    </div>
</template>

<script>
export default {
    layout: "LoginLayout",
    data() {
        return {
            form: {
                username: "",
                password: "",
                checked: [],
            },
            show: true,
        };
    },
    methods: {
        async onSubmit() {
            let username = this.form.username;
            let password = this.form.password;
            let checked = this.form.checked;
            this.$store.dispatch("accessToken", {
                username: username,
                password: password,
            });
        },
        async onReset() {
            // Reset our form values
            this.form.email = "";
            this.form.password = "";
            this.form.checked = [];
            // Trick to reset/clear native browser form validation state
            this.show = false;
            this.$nextTick(() => {
                this.show = true;
            });
        },
    },
};
</script>

<style></style>
