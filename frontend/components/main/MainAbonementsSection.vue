<script lang="ts" setup>
import type { IMainAbonementResponse } from "~/types";

defineProps<{ abonements: IMainAbonementResponse[] }>();
</script>
<template>
  <section id="main-abonements-section" class="main-abonements-section">
    <div class="container">
      <h2
        class="main-abonements-section__title"
        data-aos="zoom-in"
        data-aos-duration="1000"
      >
        Наши абонементы <BaseDot />
      </h2>
      <div class="main-abonement-section__wraper">
        <ul class="main-abonements-section__wraper-list">
          <AbonementCardByMainPage
            v-for="(abon, idx) in abonements"
            :key="abon.title"
            :plan="abon"
            data-aos="fade-up"
            :data-aos-delay="idx * 200"
          />
        </ul>
      </div>
    </div>
  </section>
</template>
<style lang="scss" scoped>
.main-abonements-section {
  padding-block: 100px;
  padding-inline: 10px;
  background-color: $bg_block;
  @include mediaMobile {
    padding-inline: 20px;
  }
  @include mediaTablet {
    padding-inline: 0px;
  }

  &__title {
    color: $accent;
    font-size: 2rem;
    margin-bottom: 4rem;
    text-align: center;
  }
  &__wraper-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;

    @include mediaTablet {
      grid-template-columns: repeat(2, 1fr);
      gap: 50px;
    }
    @include mediaLaptop {
      grid-template-columns: repeat(3, 1fr);
    }
  }
}
</style>
