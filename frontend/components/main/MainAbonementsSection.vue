<script lang="ts" setup>
import type { IMainAbonementResponse } from "~/types";

defineProps<{ abonements: IMainAbonementResponse[] }>();
</script>
<template>
  <section id="main-abonements-section" class="main-abonements-section">
    <div
      class="main-abonement-section__wraper container"
      data-aos="fade-up"
      data-aos-duration="1000"
    >
      <ul class="main-abonements-section__wraper-list">
        <AbonementCardByMainPage
          v-for="abon in abonements"
          :key="abon.title"
          :plan="abon"
        />
      </ul>
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
