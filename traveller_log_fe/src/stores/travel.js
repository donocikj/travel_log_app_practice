import { ref } from "vue";
import { defineStore } from "pinia";
import { getTravels } from "../apicalls/travelCalls";

export const useTravelStore = defineStore({
    id: 'travel',
    state: () => ({
        travels: ref([]),


    }),
    getters: {},
    actions: {
        async getTravels(offset=0, pageSize=10, filters) {
            // make a call
            let travels = await getTravels(offset, pageSize, filters)
            // store result in the store
            this.travels = travels
            console.log('retrieved travels:')
            console.log(travels)
        }
    }
});