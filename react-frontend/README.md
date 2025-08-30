# KidneyAI Pro - React Frontend

Professional React + Tailwind CSS frontend for AI-powered kidney stone detection system.

## 🚀 Features

- **Modern Dashboard**: Professional healthcare SaaS interface
- **Drag & Drop Upload**: Intuitive image upload with preview
- **Real-time Analysis**: AI-powered kidney stone detection
- **Interactive Results**: Circular progress indicators and confidence scoring
- **Scan History**: Local storage with trend visualization
- **Grad-CAM Visualization**: AI explainability with heatmap overlay
- **Dark Mode**: Toggle between light and dark themes
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Medical Color Palette**: Healthcare-focused design system

## 🛠️ Tech Stack

- **React 18** - Modern React with hooks
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Smooth animations and transitions
- **React Router** - Client-side routing
- **Recharts** - Data visualization and charts
- **Lucide React** - Beautiful icon library
- **React Dropzone** - File upload functionality
- **Vite** - Fast build tool and dev server

## 📦 Installation

```bash
# Navigate to frontend directory
cd react-frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## 🎨 Design System

### Color Palette
- **Primary**: `#1E88E5` (Teal Blue)
- **Secondary**: `#43A047` (Medical Green)
- **Danger**: `#E53935` (Error Red)
- **Warning**: `#FBC02D` (Amber Yellow)
- **Surface**: `#FFFFFF` (White)
- **Background**: `#F5F5F5` (Soft Gray)
- **Text Primary**: `#212121` (Dark Charcoal)

### Typography
- **Font**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700, 800

## 📱 Pages

1. **Dashboard** (`/`) - Overview with stats and charts
2. **Upload** (`/upload`) - Image upload and analysis
3. **History** (`/history`) - Scan history with trends
4. **About** (`/about`) - System information and disclaimer
5. **Contact** (`/contact`) - Contact form and support

## 🔧 Configuration

### Tailwind Config
Medical color palette and custom animations are configured in `tailwind.config.js`.

### API Integration
Update the backend URL in upload page:
```javascript
const BACKEND_URL = "http://localhost:8000"
```

## 🚀 Deployment

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

## 📋 Features Checklist

- ✅ Responsive sidebar navigation
- ✅ Dark mode toggle
- ✅ Drag & drop file upload
- ✅ Circular progress indicators
- ✅ Local storage for history
- ✅ Interactive charts (Recharts)
- ✅ Smooth animations (Framer Motion)
- ✅ Medical color palette
- ✅ Professional healthcare UI
- ✅ Mobile responsive design

## 🔮 Future Enhancements

- [ ] PDF report generation
- [ ] Multi-language support
- [ ] Bulk upload functionality
- [ ] Advanced filtering in history
- [ ] Real-time notifications
- [ ] User authentication
- [ ] Cloud storage integration

## 📄 License

This project is for educational and research purposes only. Not intended for actual medical diagnosis.

---

**Built with ❤️ for medical AI applications**