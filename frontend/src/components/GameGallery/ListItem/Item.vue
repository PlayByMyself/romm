<script setup>
import { ref, inject } from 'vue'
import { downloadRom, downloadSave } from '@/services/download.js'
import { storeDownloading } from '@/stores/downloading.js'

// Props
const props = defineProps(['rom'])
const forceImgReload = Date.now()
const saveFiles = ref(false)
const downloading = storeDownloading()

// Event listeners bus
const emitter = inject('emitter')
</script>

<template>
    <v-row no-gutters>
        <v-col>
            <v-list-item 
                :to="`/platform/${$route.params.platform}/rom/${rom.id}`"
                :value="rom.id"
                :key="rom.id">
                <v-row class="text-subtitle-2 align-center">
                    <v-col cols="9" xs="9" sm="6" md="3" lg="3"><span>{{ rom.r_name }}</span></v-col>
                    <v-col md="4" lg="4" class="hidden-sm-and-down"><span>{{ rom.file_name }}</span></v-col>
                    <v-col md="1" lg="1" class="hidden-sm-and-down"><span>{{ rom.p_slug }}</span></v-col>
                    <v-col sm="2" md="2" lg="2" class="hidden-xs"><span>{{ rom.file_size }} {{ rom.file_size_units }}</span></v-col>
                    <v-col sm="1" md="1" lg="1" class="hidden-xs"><span>{{ rom.region }}</span></v-col>
                    <v-col sm="1" md="1" lg="1" class="hidden-xs"><span>{{ rom.revision }}</span></v-col>
                </v-row>
                
                <template v-slot:prepend>
                    <v-avatar :rounded="0">
                        <v-progress-linear color="rommAccent1" :active="downloading.value.includes(rom.file_name)" :indeterminate="true" absolute/>
                        <v-img
                        :src="'/assets/romm/resources/'+rom.path_cover_s+'?reload='+forceImgReload"
                        :lazy-src="'/assets/romm/resources/'+rom.path_cover_s+'?reload='+forceImgReload"
                        min-height="150"/>
                    </v-avatar>
                </template>
            </v-list-item>
        </v-col>
        <v-col cols="3" xs="3" sm="1" md="1" lg="1" class="d-flex justify-center align-center mr-4">
            <v-btn
                @click="downloadRom(rom, emitter)"
                icon="mdi-download"
                size="x-small"
                variant="text"/>
            <v-btn
                @click="downloadSave(rom, emitter)"
                icon="mdi-content-save-all"
                size="x-small"
                variant="text"
                :disabled="!saveFiles"/>
            <v-btn
                @click=""
                icon="mdi-dots-vertical"
                size="x-small"
                variant="text"
                :disabled="!saveFiles"/>
        </v-col>
    </v-row>
</template>