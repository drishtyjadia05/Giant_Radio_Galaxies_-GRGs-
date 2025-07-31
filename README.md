# Unraveling the Central Engine of Giant Radio Galaxies (GRGs)

**Author**: Drishty B. Jadia  
**Project Duration**: November 2024 – January 2025  
**Mentor**: Prof. [Vaidehi S. Paliya](https://www.iucaa.in/en/faculty-research/vaidehi-paliya)  
**Institution**: [Inter-University Centre for Astronomy and Astrophysics (IUCAA)](https://www.iucaa.in/en/), Pune  

---

## Abstract

Giant Radio Galaxies (GRGs) are active galactic nuclei that host enormous, ~Mpc-scale relativistic jets — the largest structures known to be produced by individual galaxies. Despite their scale, the connection between these jets and their central engines, namely the accretion disk and supermassive black hole, remains poorly understood. In this project, we investigate the accretion properties and X-ray spectral behavior of GRGs using **Chandra** and **SDSS** observations of **LOFAR-detected** sources. Optical spectroscopy provides insights into the nature of the accretion flow (radiatively efficient or inefficient), while X-ray data help trace the emission origin — whether jet-linked or corona-dominated. Together, these diagnostics aim to shed light on the physical link between relativistic jets and their launching mechanisms.

---

## Objectives

- Classify GRGs into **HERGs (High-Excitation Radio Galaxies)** and **LERGs (Low-Excitation Radio Galaxies)** using SDSS optical spectra.
- Analyze **X-ray spectra** from Chandra observations to determine spectral parameters (e.g., photon index, flux, excess emission).
- Investigate whether observed X-ray features are consistent with **jet-dominated** or **corona-dominated** emission models.
- Identify peculiar cases showing **extended X-ray jets**, **soft excess**, or **non-standard morphologies**.

---

## Methodology

- Retrieved Chandra data and extracted X-ray spectra using the [**CIAO**] (https://cxc.cfa.harvard.edu/ciao/) software suite.
- Modeled X-ray spectra using [**XSPEC**](https://heasarc.gsfc.nasa.gov/xanadu/xspec/), fitting absorbed power-law models and computing photon indices (Γ).
- Cross-referenced optical spectra from **SDSS**, visually inspecting over 3500 spectra to classify sources based on excitation lines.
- Compared X-ray properties against radio morphology to assess alignment with jet or accretion-dominated models.

---

## 🛠️ Tools & Technologies

| Category        | Tools / Packages Used                         |
|----------------|-----------------------------------------------|
| X-ray Analysis | CIAO, XSPEC                                   |
| Optical Data   | SDSS archive, manual spectral inspection      |
| Classification | Emission-line diagnostics (HERG/LERG)         |
| Scripting      | Python, Bash                                  |
| Visualization  | Matplotlib, DS9                               |

---

## Resources

- [GRG Review paper](https://www.ias.ac.in/public/Volumes/joaa/044/00/0013.pdf)
- [Slides](https://docs.google.com/presentation/d/1WD_pHSzb5RbgGd2KY3c48NTCwpc8vY07Ovhze4ZpZfM/edit?usp=sharing) 
- To produce radio [contours](./contour.py) of LOFAR image in [DS9](https://sites.google.com/cfa.harvard.edu/saoimageds9)
- [Image Reviewer](./image_reviewer_1.py) to characterise the spectra
- To download the SDSS spectra from the list of sources - [query](./sdss_spec_query.py)
- X-ray properties of AGN - [paper](./Ricci_2017_ApJS.pdf)
- LOFAR [catalogue](https://arxiv.org/abs/2405.00232)
- XSPEC [tutorial](./vignali_xspec_tutorial_aa2022-23.pdf)

---

## Outcomes

- Identified multiple GRGs showing signs of **radiatively inefficient accretion** (LERGs) based on weak line features and hard X-ray spectra.
- Observed trends between **photon index (Γ)** and morphological classifications, suggesting a possible correlation between X-ray hardness and jet activity.
- Flagged a few GRGs with **extended X-ray jets** and **soft excess**, warranting deeper follow-up and spectral decomposition.

---

## Contact

> dbjadia05@gmail.com

---

