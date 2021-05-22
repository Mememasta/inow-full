<template>
    <div>
        <br>
        <div class="container">
            <h4> Создание мероприятия </h4>
        </div>
        <br>

        <div class="container">

        <form action="" method="POST" enctype="multipart/form-data" accept-charset="utf-8"  class="needs-validation" novalidate>

            <div class="form-group">
            <label for="inputName">Название мероприятия</label>
            <input type="text" name='name' class="form-control" id="inputName" placeholder="Название мероприятия" required>
            </div>

            <div class="form-group">
            <label for="inputAdrres">Адрес</label>
            <input type="text" name='adrres' class="form-control" id="inputAdrres" placeholder="Адрес" required>
            </div>

            <input type="text" name="author_id" hidden value="">

            <div class="form-group">
            <label for="inputDescription">Описание мероприятия</label>
            <textarea type="text" name='description' class="form-control" id="inputDescription" placeholder="Описание мероприятия" required></textarea>
            </div>

            <p>
                <label for="date">Дата: </label>
                <br>
                <input type="date" id="date" name="deadline" required />
            </p>

            <div class="form-group">
            <label for="inputContact">Контакты</label>
            <input type="text" class="form-control" name='contact' id="inputContact" placeholder="Контакты" required>
            </div>
            
            <input type="submit" class="btn btn-primary" value="Добавить мероприятие" />

        </form>

        </div>
        <br>
    </div>
</template>

<script>
export default {
  layout: "MainLayout",
  }
</script>