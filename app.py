import streamlit as st
import json
import os
from datetime import datetime

# Chemin des fichiers
DATA_FILE = os.path.join(os.path.dirname(__file__), "patates_data.json")
ASSETS_IMG = os.path.join(os.path.dirname(__file__), "assets", "wanted_quentin.jpg")
ADMIN_PASSWORD = "quentinPatate776"

# Configuration de la page
st.set_page_config(
    page_title="WANTED : QUENTIN - Avis de Recherche",
    page_icon="🥔",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Fonction de chargement des données
def load_data():
    default_data = {
        "potato_count": 42,
        "avg_potato_weight_kg": 0.15,
        "history": [
            {
                "date": "2026-09-14 00:00:00",
                "action": "+42",
                "reason": "Dette initiale certifiée par le Tribunal de l'Ouest Sauvage",
                "count_after": 42
            }
        ]
    }
    if not os.path.exists(DATA_FILE):
        save_data(default_data)
        return default_data
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default_data

# Fonction de sauvegarde des données
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

data = load_data()

# Styles CSS personnalisés - Ambiance Far West / Wanted Poster
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rye&family=Smokum&family=Cinzel:wght@700;900&family=Special+Elite&display=swap');

/* Fond général en bois de Saloon */
.stApp {
    background-color: #2b1d0c;
    background-image: radial-gradient(#3a2613 15%, transparent 16%), radial-gradient(#1e1308 15%, transparent 16%);
    background-size: 60px 60px;
    background-position: 0 0, 30px 30px;
    color: #2a1a08;
    font-family: 'Special Elite', cursive, monospace;
}

/* Conteneur de l'affiche Wanted */
.wanted-poster {
    background: #f4ecd8;
    background-image: linear-gradient(135deg, #efe3c3 0%, #f7f1e1 50%, #e8d9b5 100%);
    border: 12px double #4a2e12;
    box-shadow: 0 15px 35px rgba(0,0,0,0.8), inset 0 0 80px rgba(120, 80, 40, 0.25);
    padding: 35px 25px;
    border-radius: 6px;
    text-align: center;
    position: relative;
    margin-bottom: 25px;
}

/* Punaises sur l'affiche */
.wanted-poster::before, .wanted-poster::after {
    content: '';
    position: absolute;
    width: 18px;
    height: 18px;
    background: radial-gradient(circle at 30% 30%, #a8a8a8, #2b2b2b);
    border-radius: 50%;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.6);
    top: 10px;
}
.wanted-poster::before { left: 15px; }
.wanted-poster::after { right: 15px; }

/* Typographie Wanted */
.wanted-header {
    font-family: 'Rye', serif;
    font-size: 3.6rem;
    letter-spacing: 6px;
    color: #2b1808;
    margin: 0;
    line-height: 1.1;
    text-shadow: 2px 2px 0px #d4b886;
}

.wanted-sub {
    font-family: 'Cinzel', serif;
    font-size: 1.4rem;
    font-weight: 900;
    letter-spacing: 4px;
    color: #8b1e0f;
    border-top: 3px solid #5a3818;
    border-bottom: 3px solid #5a3818;
    display: inline-block;
    padding: 6px 20px;
    margin: 12px 0 16px 0;
    text-transform: uppercase;
}

.wanted-crime {
    font-size: 1.05rem;
    font-style: italic;
    color: #49331e;
    margin-bottom: 20px;
    line-height: 1.4;
}

/* Boîte de récompense / Prime */
.bounty-box {
    background: #2b1808;
    color: #f7e6c4;
    border: 4px solid #b8860b;
    padding: 20px;
    margin: 20px 0;
    border-radius: 4px;
    box-shadow: inset 0 0 20px rgba(0,0,0,0.8);
}

.bounty-title {
    font-family: 'Rye', serif;
    font-size: 1.6rem;
    color: #e5b95c;
    letter-spacing: 3px;
    margin-bottom: 5px;
}

.bounty-number {
    font-family: 'Smokum', cursive;
    font-size: 4.8rem;
    line-height: 1;
    color: #ffde59;
    text-shadow: 3px 3px 0px #8b1e0f;
    margin: 10px 0;
}

.bounty-currency {
    font-family: 'Cinzel', serif;
    font-size: 1.5rem;
    letter-spacing: 3px;
    color: #f7e6c4;
    font-weight: bold;
}

/* Grille des équivalences */
.stat-card {
    background: #e9dec4;
    border: 2px dashed #6d4a27;
    border-radius: 6px;
    padding: 16px 12px;
    text-align: center;
    margin-bottom: 12px;
}

.stat-icon {
    font-size: 2rem;
    margin-bottom: 4px;
}

.stat-value {
    font-family: 'Rye', serif;
    font-size: 1.8rem;
    color: #3b220c;
    margin: 4px 0;
}

.stat-label {
    font-family: 'Cinzel', serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: #6e4822;
    text-transform: uppercase;
}

.stat-detail {
    font-size: 0.8rem;
    color: #5c432d;
    margin-top: 4px;
}

/* Tampon "WANTED" */
.stamp {
    display: inline-block;
    padding: 4px 14px;
    text-transform: uppercase;
    font-family: 'Cinzel', serif;
    font-weight: 900;
    font-size: 1.3rem;
    color: #9e1b0e;
    border: 3px solid #9e1b0e;
    border-radius: 8px;
    transform: rotate(-5deg);
    margin: 10px 0;
    letter-spacing: 3px;
    mask-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8));
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #1e1308 !important;
    border-right: 3px solid #5a3818;
}

[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
    font-family: 'Rye', serif !important;
    color: #e5b95c !important;
}

[data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
    color: #dfcfb2 !important;
}
</style>
""", unsafe_allow_html=True)

# Variables dynamiques de calcul
potato_count = int(data.get("potato_count", 0))
avg_weight = float(data.get("avg_potato_weight_kg", 0.15))

total_weight_kg = potato_count * avg_weight
bags_1kg = total_weight_kg / 1.0
full_bags_1kg = int(total_weight_kg // 1.0)
remaining_grams = int(round((total_weight_kg - full_bags_1kg) * 1000))

# Calculs amusants
portions_frites = int(total_weight_kg / 0.20)  # 200g par barquette
kilos_puree = round(total_weight_kg * 1.25, 1)  # avec beurre et lait
raclettes_sauvees = int(potato_count / 4) if potato_count >= 4 else 0

# --- AFFICHAGE PRINCIPAL (Affiche Wanted) ---
st.markdown("""
<div class="wanted-poster">
    <div class="wanted-header">WANTED</div>
    <div class="wanted-sub">☠️ RECHERCHÉ MORT OU VIF ☠️</div>
    <div class="wanted-crime">
        <strong>INDIVIDU :</strong> QUENTIN DIT <em>« LE BANDIT DES BACQUETS »</em><br>
        <strong>CHEF D'ACCUSATION :</strong> DÉLIT DE FUITE & DETTE AMYLACÉE NON HONORÉE
    </div>
""", unsafe_allow_html=True)

# Affichage de l'image de Quentin / Bandit
if os.path.exists(ASSETS_IMG):
    col_l, col_img, col_r = st.columns([1, 4, 1])
    with col_img:
        st.image(ASSETS_IMG, use_container_width=True, caption="Dernière apparition connue de Quentin près d'un champ de patates")

st.markdown(f"""
    <div class="bounty-box">
        <div class="bounty-title">⭐ PRIME EXIGÉE ⭐</div>
        <div class="bounty-number">{potato_count:,}</div>
        <div class="bounty-currency">PATATES FERMES ET RÉCOLTÉES</div>
    </div>
    
    <div class="stamp">DÉPÔT IMMÉDIAT EXIGÉ</div>
</div>
""", unsafe_allow_html=True)

# --- STATISTIQUES ET CONVERSIONS DYNAMIQUES ---
st.markdown("### 📜 ÉQUIVALENCE DU BUTIN")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-icon">🥔</div>
        <div class="stat-label">Total Patates</div>
        <div class="stat-value">{potato_count}</div>
        <div class="stat-detail">Unités dues à la virgule près</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    weight_display = f"{total_weight_kg:.2f} kg" if total_weight_kg < 1000 else f"{(total_weight_kg/1000):.3f} T"
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-icon">⚖️</div>
        <div class="stat-label">Poids Total</div>
        <div class="stat-value">{weight_display}</div>
        <div class="stat-detail">Base : ~{int(avg_weight*1000)}g par patate</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-icon">🛍️</div>
        <div class="stat-label">Sacs de 1 kg</div>
        <div class="stat-value">{bags_1kg:.1f}</div>
        <div class="stat-detail">{full_bags_1kg} sac(s) + {remaining_grams}g</div>
    </div>
    """, unsafe_allow_html=True)

# Ligne d'équivalences culinaires
st.markdown("#### 🍟 Conversion en denrées du Far West")
c_frite, c_puree, c_raclette = st.columns(3)
with c_frite:
    st.info(f"🍟 **{portions_frites}** cornets de frites de Saloon (200g/portion)")
with c_puree:
    st.success(f"🥣 **{kilos_puree} kg** de purée onctueuse au beurre")
with c_raclette:
    st.warning(f"🧀 **{raclettes_sauvees}** repas raclette sauvés (4 patates/personne)")

# Avis de prime solennel
st.markdown("""
> 🤠 **Avis du Shérif :** *Toute personne apercevant Quentin est priée de lui rappeler avec insistance qu'une dette de féculents ne s'efface jamais avec le vent des plaines.*
""")

# --- ESPACE ADMINISTRATEUR (SIDEBAR) ---
with st.sidebar:
    st.markdown("## 🔐 Bureau du Shérif")
    st.markdown("*Zone réservée au recouvreur de dette.*")

    admin_input = st.text_input(
        "Code d'accès Shérif / Admin :",
        type="password",
        placeholder="Entrez le code secret..."
    )

    is_admin = (admin_input == ADMIN_PASSWORD)

    if admin_input and not is_admin:
        st.error("❌ Mauvais code ! Quentin continue sa cavale...")

    if is_admin:
        st.success("✅ Accès Shérif déverrouillé !")
        st.markdown("---")
        st.markdown("### ⚙️ Ajuster la dette")

        # Ajustement direct
        new_count = st.number_input(
            "Modifier le nombre de patates :",
            min_value=0,
            max_value=1_000_000,
            value=potato_count,
            step=1
        )

        reason = st.text_input(
            "Motif de l'ajustement :",
            placeholder="Ex: A encore parié et perdu au poker du saloon..."
        )

        if st.button("💾 Enregistrer le nouveau solde", use_container_width=True):
            diff = new_count - potato_count
            action_text = f"{'+' if diff >= 0 else ''}{diff}"
            data["potato_count"] = int(new_count)
            data.setdefault("history", []).insert(0, {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "action": action_text,
                "reason": reason if reason.strip() else "Mise à jour directe du Shérif",
                "count_after": int(new_count)
            })
            save_data(data)
            st.toast("✅ Dette mise à jour avec succès !", icon="🥔")
            st.rerun()

        # Boutons d'action rapide
        st.markdown("#### ⚡ Ajouts / Retraits rapides")
        btn_col1, btn_col2 = st.columns(2)
        
        with btn_col1:
            if st.button("+1 🥔", use_container_width=True):
                data["potato_count"] += 1
                data.setdefault("history", []).insert(0, {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "action": "+1",
                    "reason": "Pénalité rapide (+1)",
                    "count_after": data["potato_count"]
                })
                save_data(data)
                st.rerun()
            if st.button("+5 🥔", use_container_width=True):
                data["potato_count"] += 5
                data.setdefault("history", []).insert(0, {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "action": "+5",
                    "reason": "Amende salée (+5)",
                    "count_after": data["potato_count"]
                })
                save_data(data)
                st.rerun()
            if st.button("+20 🥔", use_container_width=True):
                data["potato_count"] += 20
                data.setdefault("history", []).insert(0, {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "action": "+20",
                    "reason": "Gros litige de patates (+20)",
                    "count_after": data["potato_count"]
                })
                save_data(data)
                st.rerun()

        with btn_col2:
            if st.button("-1 🥔", use_container_width=True):
                if data["potato_count"] > 0:
                    data["potato_count"] -= 1
                    data.setdefault("history", []).insert(0, {
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "action": "-1",
                        "reason": "Remboursement partiel (-1)",
                        "count_after": data["potato_count"]
                    })
                    save_data(data)
                    st.rerun()
            if st.button("-5 🥔", use_container_width=True):
                new_val = max(0, data["potato_count"] - 5)
                data["potato_count"] = new_val
                data.setdefault("history", []).insert(0, {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "action": "-5",
                    "reason": "Remboursement (-5)",
                    "count_after": data["potato_count"]
                })
                save_data(data)
                st.rerun()
            if st.button("Tout éponger (0 🥔)", use_container_width=True):
                data["potato_count"] = 0
                data.setdefault("history", []).insert(0, {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "action": "RESET 0",
                    "reason": "Quentin a enfin payé sa dette !",
                    "count_after": 0
                })
                save_data(data)
                st.rerun()

        st.markdown("---")
        # Paramètres avancés
        with st.expander("⚖️ Calibrage du poids moyen d'une patate"):
            custom_weight_g = st.slider(
                "Poids unitaire en grammes :",
                min_value=50,
                max_value=400,
                value=int(avg_weight * 1000),
                step=10
            )
            if st.button("Valider le calibre"):
                data["avg_potato_weight_kg"] = custom_weight_g / 1000.0
                save_data(data)
                st.toast(f"Calibre fixé à {custom_weight_g}g par patate")
                st.rerun()

        # Historique
        with st.expander("📜 Registre des méfaits (Historique)"):
            history = data.get("history", [])
            if history:
                for h in history[:10]:
                    st.markdown(f"**{h.get('date', '')}** : `{h.get('action', '')}` (Total: {h.get('count_after', '')})")
                    st.caption(f"_{h.get('reason', '')}_")
                    st.markdown("---")
            else:
                st.write("Aucun historique pour le moment.")

    else:
        st.info("🔒 Entrez le code secret Shérif pour administrer le solde de patates.")
