<script setup>
// this comp should receive travel object with entries array as a props.
import { defineProps, ref } from 'vue';

let collapsed = ref(true);

const props = defineProps(["travel"]);
// it should also have a flag for whether the view is collapsed, showing only title and author, or the full content?
// it should also have options if author of the travel is logged in to remove the travel (with confirmation popup?), 
//      edit individual entries (maybe job for another component) or create new entry
// maybe just entry id for loading when necessary?
</script>

<template>
    <div class="travelcomp" @click="collapsed = !collapsed">
        <p>travel id: {{ props.travel.id }}, travel title: {{ props.travel.title }}, traveller id: {{ props.travel.traveller }}</p>
        <!-- todo show entries (based on collapsed state) -->
        <div v-if="!collapsed">
            <p>entries come here</p>
        </div>
        <!-- todo: some additional options if logged in user id === traveller id (remove, edit...) -->
    </div>
</template>