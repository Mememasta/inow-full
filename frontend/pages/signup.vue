<template>
    <div class="card container form-signin text-center" style="width: 40em; border-radius: 15px">
        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <h1 class="h3 m-4 font-weight-normal">Регистрация</h1>
            <b-form-group
                id="email"
                label-for="email"
            >
            <b-form-input
                id="email"
                v-model="form.email"
                type="email"
                required
                placeholder="Введите email"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="password"
                label-for="password"
            >
            <b-form-input
                id="password"
                v-model="form.password"
                type="password"
                required
                placeholder="Введите пароль"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="secondname"
                label-for="secondname"
            >
            <b-form-input
                id="secondname"
                v-model="form.secondname"
                type="text"
                required
                placeholder="Введите имя"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="name"
                label-for="name"
            >
            <b-form-input
                id="name"
                v-model="form.name"
                type="text"
                required
                placeholder="Введите фамилию"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-4">
                <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
                    <b-form-checkbox value="true">Я согласен на обработку персональных данных</b-form-checkbox>
                </b-form-checkbox-group>
            </b-form-group>

            <b-button type="submit" variant="primary" block>Зарегистрироваться</b-button>
            
            <br>

            <NuxtLink to="/login">У меня есть профиль</NuxtLink> | <NuxtLink to="/">Главная</NuxtLink>
            <p class="mt-3 mb-3 text-muted">&copy; 2021</p>

        </b-form>
    </div>
</template>

<script>
  export default {
    middleware: 'quest',
    layout: "LoginLayout",
    data() {
      return {
          email: '',
          password: '',
          name: '',
          secondname: '',
          show: true,
          error: ''
        };
    },
    methods: {
        async register() {
          try {
            await this.$axios.post('users/open', {
                email: this.email,
                password: this.password
            })
            const params = new URLSearchParams();
            params.append('username', this.email);
            params.append('password', this.password);
            await this.$auth.loginWith('local', {
              data: params
            })

            this.$nuxt.$router.replace({ path: '/'})
          } catch (e) {
            this.error = e.response
          }
        }
    }
  }
</script>
