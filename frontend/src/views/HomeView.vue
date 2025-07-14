<template>
  <div class="min-h-screen cafe-bg">
    <!-- Hero Section -->
    <section class="relative py-20 px-4">
      <div class="max-w-6xl mx-auto text-center">
        <h1 class="text-5xl font-bold forest-green mb-6">Apaiser Café</h1>
        <p class="text-xl text-gray-700 mb-8">森の中の穏やかなカフェで、心安らぐひとときを</p>
        <div class="flex justify-center space-x-4">
          <button 
            @click="scrollToReservation"
            class="bg-green-600 text-white px-8 py-3 rounded-lg hover:bg-green-700 transition-colors"
          >
            ご予約はこちら
          </button>
          <button 
            @click="scrollToMenu"
            class="bg-amber-600 text-white px-8 py-3 rounded-lg hover:bg-amber-700 transition-colors"
          >
            メニューを見る
          </button>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section class="py-16 px-4">
      <div class="max-w-4xl mx-auto">
        <div class="cafe-card rounded-lg p-8 mb-12">
          <h2 class="text-3xl font-bold forest-green mb-6 text-center">カフェについて</h2>
          <p class="text-gray-700 leading-relaxed mb-4">
            Apaiser Caféは、フランス語で「穏やかにする」という意味を持つ、森の中の静かなカフェです。
            自然に囲まれた落ち着いた空間で、厳選されたコーヒーと手作りのスイーツをお楽しみいただけます。
          </p>
          <p class="text-gray-700 leading-relaxed">
            忙しい日常から離れて、ゆったりとした時間をお過ごしください。
            読書やお仕事、友人との語らいなど、様々なシーンでご利用いただけます。
          </p>
        </div>
      </div>
    </section>

    <!-- Announcements Section -->
    <section class="py-16 px-4 bg-white bg-opacity-50">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-3xl font-bold forest-green mb-8 text-center">お知らせ</h2>
        <div class="space-y-6">
          <div 
            v-for="announcement in announcements.slice(0, 3)" 
            :key="announcement.id"
            class="cafe-card rounded-lg p-6"
          >
            <h3 class="text-xl font-semibold warm-brown mb-2">{{ announcement.title }}</h3>
            <p class="text-gray-700 mb-2">{{ announcement.content }}</p>
            <p class="text-sm text-gray-500">{{ formatDate(announcement.created_at) }}</p>
          </div>
        </div>
        <div class="text-center mt-8">
          <router-link 
            to="/announcements" 
            class="text-green-600 hover:text-green-700 font-medium"
          >
            すべてのお知らせを見る →
          </router-link>
        </div>
      </div>
    </section>

    <!-- Menu Section -->
    <section id="menu" class="py-16 px-4">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold forest-green mb-12 text-center">メニュー</h2>
        <div class="grid md:grid-cols-2 gap-8">
          <div class="cafe-card rounded-lg p-6">
            <h3 class="text-2xl font-semibold warm-brown mb-4">ドリンク</h3>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span>ブレンドコーヒー</span>
                <span class="font-medium">¥450</span>
              </div>
              <div class="flex justify-between">
                <span>カフェラテ</span>
                <span class="font-medium">¥520</span>
              </div>
              <div class="flex justify-between">
                <span>季節限定 桜ラテ</span>
                <span class="font-medium">¥580</span>
              </div>
              <div class="flex justify-between">
                <span>紅茶各種</span>
                <span class="font-medium">¥400</span>
              </div>
            </div>
          </div>
          <div class="cafe-card rounded-lg p-6">
            <h3 class="text-2xl font-semibold warm-brown mb-4">フード・デザート</h3>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span>手作りチーズケーキ</span>
                <span class="font-medium">¥480</span>
              </div>
              <div class="flex justify-between">
                <span>抹茶チーズケーキ</span>
                <span class="font-medium">¥520</span>
              </div>
              <div class="flex justify-between">
                <span>本日のケーキ</span>
                <span class="font-medium">¥450</span>
              </div>
              <div class="flex justify-between">
                <span>サンドイッチセット</span>
                <span class="font-medium">¥780</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Business Hours & Access -->
    <section class="py-16 px-4 bg-white bg-opacity-50">
      <div class="max-w-6xl mx-auto">
        <div class="grid md:grid-cols-2 gap-12">
          <!-- Business Hours -->
          <div class="cafe-card rounded-lg p-6">
            <h3 class="text-2xl font-semibold forest-green mb-4">営業時間</h3>
            <div class="space-y-2">
              <div class="flex justify-between">
                <span>平日</span>
                <span>9:00 - 20:00</span>
              </div>
              <div class="flex justify-between">
                <span>土日祝</span>
                <span>9:00 - 21:00</span>
              </div>
              <div class="mt-4 text-sm text-gray-600">
                <p>定休日: 毎週火曜日</p>
                <p>※祝日の場合は営業いたします</p>
              </div>
            </div>
          </div>

          <!-- Contact Info -->
          <div class="cafe-card rounded-lg p-6">
            <h3 class="text-2xl font-semibold forest-green mb-4">アクセス・お問い合わせ</h3>
            <div class="space-y-2">
              <p><strong>住所:</strong> 栃木県宇都宮市塙田1-1-20</p>
              <p><strong>電話:</strong> 028-623-1234</p>
              <p><strong>メール:</strong> info@apaiser-cafe.com</p>
              <p class="text-sm text-gray-600 mt-4">
                栃木県庁より徒歩5分<br>
                駐車場完備（20台）
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Google Maps -->
    <section class="py-16 px-4">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-3xl font-bold forest-green mb-8 text-center">アクセスマップ</h2>
        <div class="cafe-card rounded-lg p-4">
          <div class="w-full h-96 rounded-lg overflow-hidden">
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3222.8234567890123!2d139.8836!3d36.5658!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601f676b1234567%3A0x1234567890abcdef!2z5qCg5pyo55yM5bqB!5e0!3m2!1sja!2sjp!4v1234567890123!5m2!1sja!2sjp"
              width="100%"
              height="100%"
              style="border:0;"
              allowfullscreen=""
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
            ></iframe>
          </div>
        </div>
      </div>
    </section>

    <!-- Reservation Section -->
    <section id="reservation" class="py-16 px-4 bg-white bg-opacity-50">
      <div class="max-w-2xl mx-auto">
        <h2 class="text-3xl font-bold forest-green mb-8 text-center">ご予約</h2>
        <div class="cafe-card rounded-lg p-8">
          <form @submit.prevent="submitReservation" class="space-y-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">お名前 *</label>
              <input
                v-model="reservation.name"
                type="text"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">電話番号 *</label>
              <input
                v-model="reservation.phone"
                type="tel"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">メールアドレス *</label>
              <input
                v-model="reservation.email"
                type="email"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">人数 *</label>
              <select
                v-model="reservation.party_size"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
              >
                <option value="">選択してください</option>
                <option v-for="i in 8" :key="i" :value="i">{{ i }}名</option>
              </select>
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">予約日時 *</label>
              <input
                v-model="reservation.reservation_date"
                type="datetime-local"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">備考</label>
              <textarea
                v-model="reservation.notes"
                rows="3"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
                placeholder="アレルギーやご要望などがございましたらお書きください"
              ></textarea>
            </div>
            
            <button
              type="submit"
              :disabled="isSubmitting"
              class="w-full bg-green-600 text-white py-3 px-4 rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 disabled:opacity-50"
            >
              {{ isSubmitting ? '送信中...' : '予約を送信' }}
            </button>
          </form>
          
          <div v-if="reservationMessage" class="mt-4 p-4 rounded-md" :class="reservationMessageClass">
            {{ reservationMessage }}
          </div>
        </div>
      </div>
    </section>
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
  updated_at: string
}

interface ReservationForm {
  name: string
  phone: string
  email: string
  party_size: number | string
  reservation_date: string
  notes: string
}

const announcements = ref<Announcement[]>([])
const reservation = ref<ReservationForm>({
  name: '',
  phone: '',
  email: '',
  party_size: '',
  reservation_date: '',
  notes: ''
})

const isSubmitting = ref(false)
const reservationMessage = ref('')
const reservationMessageClass = ref('')

const API_BASE_URL = 'http://localhost:8000'

const fetchAnnouncements = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/api/announcements`)
    announcements.value = response.data
  } catch (error) {
    console.error('Failed to fetch announcements:', error)
  }
}

const submitReservation = async () => {
  isSubmitting.value = true
  reservationMessage.value = ''
  
  try {
    const reservationData = {
      ...reservation.value,
      party_size: Number(reservation.value.party_size)
    }
    
    const response = await axios.post(`${API_BASE_URL}/api/reservations`, reservationData)
    
    reservationMessage.value = 'ご予約を承りました。確認メールをお送りいたします。'
    reservationMessageClass.value = 'bg-green-100 text-green-800 border border-green-200'
    
    // Reset form
    reservation.value = {
      name: '',
      phone: '',
      email: '',
      party_size: '',
      reservation_date: '',
      notes: ''
    }
  } catch (error) {
    console.error('Failed to submit reservation:', error)
    reservationMessage.value = 'ご予約の送信に失敗しました。もう一度お試しください。'
    reservationMessageClass.value = 'bg-red-100 text-red-800 border border-red-200'
  } finally {
    isSubmitting.value = false
  }
}

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const scrollToReservation = () => {
  document.getElementById('reservation')?.scrollIntoView({ behavior: 'smooth' })
}

const scrollToMenu = () => {
  document.getElementById('menu')?.scrollIntoView({ behavior: 'smooth' })
}

onMounted(() => {
  fetchAnnouncements()
})
</script>
