<template>
  <div class="min-h-screen bg-gray-50">
    <nav class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <router-link to="/" class="text-xl font-bold text-green-600">Apaiser Café</router-link>
            <span class="ml-4 text-gray-500">管理画面</span>
          </div>
          <div class="flex items-center space-x-4">
            <router-link to="/" class="text-gray-700 hover:text-green-600">ホーム</router-link>
            <button 
              v-if="isAuthenticated" 
              @click="logout"
              class="text-gray-700 hover:text-red-600"
            >
              ログアウト
            </button>
          </div>
        </div>
      </div>
    </nav>

    <div class="max-w-6xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
      <!-- Login Form -->
      <div v-if="!isAuthenticated" class="max-w-md mx-auto">
        <div class="bg-white rounded-lg shadow-md p-8">
          <h1 class="text-2xl font-bold text-gray-900 mb-6 text-center">管理者ログイン</h1>
          
          <form @submit.prevent="login">
            <div class="mb-4">
              <label for="username" class="block text-sm font-medium text-gray-700 mb-2">
                ユーザー名
              </label>
              <input
                id="username"
                v-model="loginForm.username"
                type="text"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              />
            </div>
            
            <div class="mb-6">
              <label for="password" class="block text-sm font-medium text-gray-700 mb-2">
                パスワード
              </label>
              <input
                id="password"
                v-model="loginForm.password"
                type="password"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent"
              />
            </div>
            
            <div v-if="loginError" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-md">
              <p class="text-red-800 text-sm">{{ loginError }}</p>
            </div>
            
            <button
              type="submit"
              :disabled="loginLoading"
              class="w-full bg-green-600 text-white py-2 px-4 rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="loginLoading">ログイン中...</span>
              <span v-else>ログイン</span>
            </button>
          </form>
        </div>
      </div>

      <!-- Admin Dashboard -->
      <div v-else>
        <h1 class="text-3xl font-bold text-gray-900 mb-8">管理画面</h1>
        
        <!-- Tab Navigation -->
        <div class="border-b border-gray-200 mb-8">
          <nav class="-mb-px flex space-x-8">
            <button
              @click="activeTab = 'announcements'"
              :class="[
                'py-2 px-1 border-b-2 font-medium text-sm',
                activeTab === 'announcements'
                  ? 'border-green-500 text-green-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              ]"
            >
              お知らせ管理
            </button>
            <button
              @click="activeTab = 'reservations'"
              :class="[
                'py-2 px-1 border-b-2 font-medium text-sm',
                activeTab === 'reservations'
                  ? 'border-green-500 text-green-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              ]"
            >
              予約管理
            </button>
          </nav>
        </div>

        <!-- Announcements Management -->
        <div v-if="activeTab === 'announcements'">
          <div class="mb-6">
            <button
              @click="showAnnouncementForm = !showAnnouncementForm"
              class="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700"
            >
              新しいお知らせを作成
            </button>
          </div>

          <!-- Announcement Form -->
          <div v-if="showAnnouncementForm" class="bg-white rounded-lg shadow-md p-6 mb-6">
            <h3 class="text-lg font-semibold mb-4">
              {{ editingAnnouncement ? 'お知らせを編集' : '新しいお知らせ' }}
            </h3>
            
            <form @submit.prevent="saveAnnouncement">
              <div class="mb-4">
                <label for="title" class="block text-sm font-medium text-gray-700 mb-2">
                  タイトル
                </label>
                <input
                  id="title"
                  v-model="announcementForm.title"
                  type="text"
                  required
                  class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
                />
              </div>
              
              <div class="mb-4">
                <label for="content" class="block text-sm font-medium text-gray-700 mb-2">
                  内容
                </label>
                <textarea
                  id="content"
                  v-model="announcementForm.content"
                  rows="4"
                  required
                  class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
                ></textarea>
              </div>
              
              <div class="flex space-x-4">
                <button
                  type="submit"
                  class="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700"
                >
                  {{ editingAnnouncement ? '更新' : '作成' }}
                </button>
                <button
                  type="button"
                  @click="cancelAnnouncementEdit"
                  class="bg-gray-300 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-400"
                >
                  キャンセル
                </button>
              </div>
            </form>
          </div>

          <!-- Announcements List -->
          <div class="bg-white rounded-lg shadow-md">
            <div class="px-6 py-4 border-b border-gray-200">
              <h3 class="text-lg font-semibold">お知らせ一覧</h3>
            </div>
            
            <div v-if="announcements.length === 0" class="p-6 text-center text-gray-500">
              お知らせがありません
            </div>
            
            <div v-else class="divide-y divide-gray-200">
              <div
                v-for="announcement in announcements"
                :key="announcement.id"
                class="p-6 hover:bg-gray-50"
              >
                <div class="flex justify-between items-start">
                  <div class="flex-1">
                    <h4 class="text-lg font-medium text-gray-900 mb-2">
                      {{ announcement.title }}
                    </h4>
                    <p class="text-gray-600 mb-2">{{ announcement.content }}</p>
                    <p class="text-sm text-gray-500">
                      {{ formatDate(announcement.created_at) }}
                    </p>
                  </div>
                  <div class="flex space-x-2 ml-4">
                    <button
                      @click="editAnnouncement(announcement)"
                      class="text-blue-600 hover:text-blue-800"
                    >
                      編集
                    </button>
                    <button
                      @click="deleteAnnouncement(announcement.id)"
                      class="text-red-600 hover:text-red-800"
                    >
                      削除
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Reservations Management -->
        <div v-if="activeTab === 'reservations'">
          <div class="bg-white rounded-lg shadow-md">
            <div class="px-6 py-4 border-b border-gray-200">
              <h3 class="text-lg font-semibold">予約一覧</h3>
            </div>
            
            <div v-if="reservations.length === 0" class="p-6 text-center text-gray-500">
              予約がありません
            </div>
            
            <div v-else class="divide-y divide-gray-200">
              <div
                v-for="reservation in reservations"
                :key="reservation.id"
                class="p-6 hover:bg-gray-50"
              >
                <div class="flex justify-between items-start">
                  <div class="flex-1">
                    <h4 class="text-lg font-medium text-gray-900 mb-2">
                      {{ reservation.name }}
                    </h4>
                    <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
                      <div>
                        <span class="font-medium">電話番号:</span> {{ reservation.phone }}
                      </div>
                      <div>
                        <span class="font-medium">メール:</span> {{ reservation.email }}
                      </div>
                      <div>
                        <span class="font-medium">人数:</span> {{ reservation.party_size }}名
                      </div>
                      <div>
                        <span class="font-medium">予約日時:</span> {{ formatDateTime(reservation.reservation_datetime) }}
                      </div>
                    </div>
                    <p class="text-sm text-gray-500 mt-2">
                      予約日: {{ formatDate(reservation.created_at) }}
                    </p>
                  </div>
                  <div class="flex space-x-2 ml-4">
                    <button
                      @click="deleteReservation(reservation.id)"
                      class="text-red-600 hover:text-red-800"
                    >
                      削除
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Announcement {
  id: number
  title: string
  content: string
  created_at: string
}

interface Reservation {
  id: number
  name: string
  phone: string
  email: string
  party_size: number
  reservation_datetime: string
  created_at: string
}

const isAuthenticated = ref(false)
const activeTab = ref('announcements')
const showAnnouncementForm = ref(false)
const editingAnnouncement = ref<Announcement | null>(null)

const loginForm = ref({
  username: '',
  password: ''
})
const loginError = ref('')
const loginLoading = ref(false)

const announcementForm = ref({
  title: '',
  content: ''
})

const announcements = ref<Announcement[]>([])
const reservations = ref<Reservation[]>([])

const login = async () => {
  try {
    loginLoading.value = true
    loginError.value = ''
    
    const response = await axios.post('http://localhost:8000/api/admin/login', {
      username: loginForm.value.username,
      password: loginForm.value.password
    })
    
    const token = response.data.access_token
    localStorage.setItem('admin_token', token)
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    
    isAuthenticated.value = true
    await fetchData()
  } catch (err) {
    console.error('Login failed:', err)
    loginError.value = 'ログインに失敗しました。ユーザー名とパスワードを確認してください。'
  } finally {
    loginLoading.value = false
  }
}

const logout = () => {
  localStorage.removeItem('admin_token')
  delete axios.defaults.headers.common['Authorization']
  isAuthenticated.value = false
  loginForm.value = { username: '', password: '' }
}

const fetchData = async () => {
  await Promise.all([fetchAnnouncements(), fetchReservations()])
}

const fetchAnnouncements = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/announcements')
    announcements.value = response.data
  } catch (err) {
    console.error('Failed to fetch announcements:', err)
  }
}

const fetchReservations = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/admin/reservations')
    reservations.value = response.data
  } catch (err) {
    console.error('Failed to fetch reservations:', err)
  }
}

const saveAnnouncement = async () => {
  try {
    if (editingAnnouncement.value) {
      await axios.put(`http://localhost:8000/api/admin/announcements/${editingAnnouncement.value.id}`, announcementForm.value)
    } else {
      await axios.post('http://localhost:8000/api/admin/announcements', announcementForm.value)
    }
    
    await fetchAnnouncements()
    cancelAnnouncementEdit()
  } catch (err) {
    console.error('Failed to save announcement:', err)
  }
}

const editAnnouncement = (announcement: Announcement) => {
  editingAnnouncement.value = announcement
  announcementForm.value = {
    title: announcement.title,
    content: announcement.content
  }
  showAnnouncementForm.value = true
}

const cancelAnnouncementEdit = () => {
  editingAnnouncement.value = null
  announcementForm.value = { title: '', content: '' }
  showAnnouncementForm.value = false
}

const deleteAnnouncement = async (id: number) => {
  if (confirm('このお知らせを削除しますか？')) {
    try {
      await axios.delete(`http://localhost:8000/api/admin/announcements/${id}`)
      await fetchAnnouncements()
    } catch (err) {
      console.error('Failed to delete announcement:', err)
    }
  }
}

const deleteReservation = async (id: number) => {
  if (confirm('この予約を削除しますか？')) {
    try {
      await axios.delete(`http://localhost:8000/api/admin/reservations/${id}`)
      await fetchReservations()
    } catch (err) {
      console.error('Failed to delete reservation:', err)
    }
  }
}

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const formatDateTime = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(() => {
  const token = localStorage.getItem('admin_token')
  if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    isAuthenticated.value = true
    fetchData()
  }
})
</script>
