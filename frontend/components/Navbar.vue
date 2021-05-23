<template>
    <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
        
        <div>
          <b-button v-b-toggle.sidebar-backdrop variant="info">Меню</b-button>
          <b-sidebar id="sidebar-backdrop" title="" backdrop shadow>
            <template #default="{ hide }">
              <div class="px-3 py-2">
                <nav class="mb-3">
                  <b-nav vertical>
                    <b-nav-item v-if="isAuthenticated" to="/users/me" @click="hide"><h2> {{ loggedInUser.first_name }} {{ loggedInUser.second_name }}</h2></b-nav-item>
                    <b-nav-item to="/events" @click="hide"> Спортиивные мероприятия </b-nav-item>
                    <b-nav-item to="/objects" @click="hide"> Спортивные объекты </b-nav-item>            
                    <b-nav-item to="/exchange" @click="hide"> Аренда от людей </b-nav-item>
                    <b-nav-item to="/services" @click="hide"> Сервисы </b-nav-item>                    
                    <b-nav-item to="/" @click="hide"> Связаться с нами (Telegram) </b-nav-item>
                    <b-nav-item v-if="isAuthenticated" to="/login" @click="logout"> Выйти </b-nav-item>                    
                    <div v-else>
                        <b-nav-item to="/signup" @click="hide"> Зарегистрироваться </b-nav-item>
                        <b-nav-item to="/login" @click="hide"> Авторизоваться </b-nav-item>
                    </div>
                  </b-nav>
                </nav>
              </div>
            </template>
          </b-sidebar>
        </div>

        <b-navbar-nav class="ml-auto">
          <b-navbar-brand to="/" right>ЯНАО-Спорт</b-navbar-brand>
        </b-navbar-nav>

      </b-navbar>
    </div>
</template>


<script>
import {mapGetters} from "vuex"
export default {
    data() {
        return {
            isActive: false,
        }
    },
    computed: {
        ...mapGetters(['isAuthenticated', 'loggedInUser'])
    },
    methods: {
        async logout() {
            await this.$auth.logout();
        }
    }

}

</script>


  
<style scoped>

</style>
        
