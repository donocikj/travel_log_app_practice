<script setup>
import {useTravelStore} from "../stores/travel.js"
import { computed } from "vue";
import TravelComp from "./TravelComp.vue"

const travelStore = useTravelStore()

travelStore.getTravels();

// const travelList = computed(()=>travelStore.travels)

</script>

<template>
    <p>this is a component for showing a list of travels.</p>
    <!-- todo: some controls for pagination -->
    <ul>
        <li v-for="travel in travelStore.travels">
            <TravelComp :travel="travel"></TravelComp>
        </li>
    </ul>
</template>